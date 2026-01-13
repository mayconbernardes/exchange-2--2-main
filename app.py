# app.py
import os
import random
import json


from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request, session, jsonify 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_socketio import SocketIO
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from flask_caching import Cache
from flask_mail import Mail
from email_validator import validate_email, EmailNotValidError
from werkzeug.exceptions import RequestEntityTooLarge
from models import User, Flashcard, TextAudioLesson, InteractiveGame, db  # Ensure these models are in models.py
from forms import UserProfileForm, FlashcardForm, LoginForm, RegistrationForm, LessonForm, GameForm, INTERESTS, LANGUAGES # Ensure these forms are in forms.py
from pymongo import MongoClient
from translations import TRANSLATIONS

# Initialize Flask app
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_very_secret_key')  # Use environment variable or a default
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://root:root@localhost/interchange')  # Use environment variable or a default
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # Increase limit to 32 MB for audio/images

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
csrf = CSRFProtect(app)
mail = Mail(app)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "500 per hour"],
    storage_uri="memory://"
)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
socketio = SocketIO(app)
Talisman(app, content_security_policy=None)
Session(app)

# MongoDB Connection
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB_NAME = 'interchange'

try:
    # Set a very short timeout for MongoDB to prevent blocking the app
    mongo_client = MongoClient(MONGO_HOST, MONGO_PORT, serverSelectionTimeoutMS=1000)
    mongo_db = mongo_client[MONGO_DB_NAME]
    # Simple ping to check connection
    mongo_client.admin.command('ping')
    print(f"Successfully connected to MongoDB: {MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}")
    mongodb_available = True
except Exception as e:
    print(f"MongoDB not available, logging will be disabled: {e}")
    mongodb_available = False

# Helper function to log user activity to MongoDB
def log_user_activity(user_id, activity_type, details=None):
    if not mongodb_available:
        return
        
    if not details:
        details = {}
    activity_log = {
        "user_id": str(user_id),
        "activity_type": activity_type,
        "timestamp": datetime.utcnow(),
        "details": details
    }
    try:
        mongo_db.user_activity_logs.insert_one(activity_log)
    except Exception as e:
        # Don't print to console every time to avoid log spam if it goes down mid-session
        pass


# Routes
# Helper function for translations in routes
def get_t(key):
    lang = session.get('lang', 'en')
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in TRANSLATIONS:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))

@app.context_processor
def inject_translations():
    lang = session.get('lang', 'en')
    def translate(key):
        return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)
    return dict(t=translate, current_lang=lang)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/legal')
def legal():
    return render_template('legal.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # Update validator messages dynamically
    form.password.validators[1].message = get_t('valid_password_min_length')
    form.password.validators[2].message = get_t('valid_password_complexity')
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(get_t('auth_flash_register_success'), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)  # Add remember functionality here
            log_user_activity(user.id, "login", {"email": user.email})
            next_page = request.args.get('next')
            flash(get_t('auth_flash_logged_in'), 'success')
            return redirect(next_page) if next_page else redirect(url_for('profile'))
        else:
            flash(get_t('auth_flash_login_failed'), 'danger')
    return render_template('login.html', title=get_t('auth_login_title'), form=form)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        log_user_activity(current_user.id, "logout", {"email": current_user.email})
    logout_user()
    
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return redirect(url_for('profile'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.native_language = form.native_language.data
        current_user.learning_language = form.learning_language.data
        
        # Combine selected interests and custom interests
        selected_interests = form.interests_selection.data
        custom_interests = [interest.strip() for interest in form.interests.data.split(',') if interest.strip()]
        all_interests = list(set(selected_interests + custom_interests))
        current_user.interests = ', '.join(all_interests)
        
        if form.profile_picture.data:
            filename = secure_filename(form.profile_picture.data.filename)
            images_dir = os.path.join(app.root_path, 'static', 'images')
            os.makedirs(images_dir, exist_ok=True)
            picture_path = os.path.join(images_dir, filename)
            form.profile_picture.data.save(picture_path)
            current_user.profile_picture = filename
        
        db.session.commit()
        flash(get_t('profile_update_success'), 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.native_language.data = current_user.native_language
        form.learning_language.data = current_user.learning_language
        
        # Populate selected interests and custom interests
        if current_user.interests:
            user_interests = [interest.strip() for interest in current_user.interests.split(',') if interest.strip()]
            form.interests_selection.data = [interest for interest in user_interests if interest in [choice[0] for choice in INTERESTS]]
            form.interests.data = ', '.join([interest for interest in user_interests if interest not in [choice[0] for choice in INTERESTS]])
        else:
            form.interests_selection.data = []
            form.interests.data = ''
    return render_template('profile.html', form=form, language_map={lang[0]: lang[1] for lang in LANGUAGES})

@app.route('/flashcards', methods=['GET', 'POST'])
@login_required
def flashcards():
    form = FlashcardForm()
    if form.validate_on_submit():
        new_flashcard = Flashcard(
            term=form.front.data,
            definition=form.back.data,
            user_id=current_user.id
        )
        db.session.add(new_flashcard)
        db.session.commit()
        flash('Flashcard created successfully!', 'success')
        log_user_activity(current_user.id, "created_flashcard", {"term": new_flashcard.term, "definition": new_flashcard.definition})
        return redirect(url_for('flashcards'))
    
    user_flashcards = Flashcard.query.filter_by(user_id=current_user.id).all()
    return render_template('flashcard.html', form=form, flashcards=user_flashcards)

@app.route('/flashcards/edit/<int:flashcard_id>', methods=['GET', 'POST'])
@login_required
def edit_flashcard(flashcard_id):
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    if flashcard.user_id != current_user.id:
        flash('You are not authorized to edit this flashcard.', 'danger')
        return redirect(url_for('flashcards'))

    form = FlashcardForm()
    if form.validate_on_submit():
        flashcard.term = form.front.data
        flashcard.definition = form.back.data
        db.session.commit()
        flash('Flashcard updated successfully!', 'success')
        log_user_activity(current_user.id, "edited_flashcard", {"flashcard_id": flashcard.id, "new_term": flashcard.term})
        return redirect(url_for('flashcards'))
    elif request.method == 'GET':
        form.front.data = flashcard.term
        form.back.data = flashcard.definition
    return render_template('flashcard.html', form=form, flashcards=[flashcard], edit_mode=True)

@app.route('/flashcards/delete/<int:flashcard_id>', methods=['POST'])
@login_required
def delete_flashcard(flashcard_id):
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    if flashcard.user_id != current_user.id:
        flash('You are not authorized to delete this flashcard.', 'danger')
        return redirect(url_for('flashcards'))

    db.session.delete(flashcard)
    db.session.commit()
    flash('Flashcard deleted successfully!', 'success')
    log_user_activity(current_user.id, "deleted_flashcard", {"flashcard_id": flashcard.id, "term": flashcard.term})
    return redirect(url_for('flashcards'))

@app.route('/user/<int:user_id>')
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)  # Fetch user by ID
    return render_template('user_profile.html', user=user)  # Render user profile template

@app.route('/audio')
@login_required
def audio():
    log_user_activity(current_user.id, "view_lessons_list")
    lessons = TextAudioLesson.query.all()
    return render_template('lessons_list.html', lessons=lessons)

@app.route('/audio/<int:lesson_id>')
@login_required
def audio_lesson(lesson_id):
    lesson = TextAudioLesson.query.get_or_404(lesson_id)
    log_user_activity(current_user.id, "view_lesson", {"lesson_id": lesson_id})
    
    # Use the content from the DB or the static file if content is pointing to a filename? 
    # Actually, the model has text_content.
    transcription = lesson.text_content
    
    return render_template('audio.html', transcription=transcription, lesson=lesson)



@app.route('/game')
def game_start():
    return redirect(url_for('game_level', level_id=1))

@app.route('/game/<int:level_id>')
@login_required
def game_level(level_id):
    # Security check: sequential level access
    if level_id > current_user.last_completed_level + 1:
        flash(f'Você precisa completar o nível {current_user.last_completed_level + 1} primeiro!', 'warning')
        return redirect(url_for('game_level', level_id=current_user.last_completed_level + 1))
    
    log_user_activity(current_user.id, "started_game_level", {"level_id": level_id})
    
    # Fetch game items for this level from the database
    game_items_db = InteractiveGame.query.filter_by(level_id=level_id).all()
    
    if not game_items_db:
        flash('Level not found in database.', 'danger')
        return redirect(url_for('profile'))

    # Total levels count from unique level_id in DB
    total_levels = db.session.query(db.func.count(db.distinct(InteractiveGame.level_id))).scalar()
    
    # Map database objects to the format expected by the template
    game_items = []
    level_title = game_items_db[0].level_title
    
    for item in game_items_db:
        game_items.append({
            'image': item.image_file_path,
            'word': item.word
        })

    # Shuffle items for the game
    random.shuffle(game_items)
    
    # Extract words and shuffle them
    words = [item['word'] for item in game_items]
    random.shuffle(words)
    
    return render_template(
        'interactive_game.html', 
        level={'title': level_title}, 
        game_items=game_items, 
        words=words,
        level_id=level_id,
        total_levels=total_levels
    )



@app.route('/game/complete/<int:level_id>', methods=['POST'])
@login_required
def complete_level(level_id):
    data = request.get_json()
    score = data.get('score', 0) if data else 0
    
    # Increment total points
    if current_user.total_points is None:
        current_user.total_points = 0
    current_user.total_points += score
    
    if level_id > current_user.last_completed_level:
        current_user.last_completed_level = level_id
        
    db.session.commit()
    log_user_activity(current_user.id, "completed_game_level", {"level_id": level_id, "score_added": score, "total_points": current_user.total_points})
    
    return jsonify({
        "status": "success", 
        "last_completed_level": current_user.last_completed_level,
        "total_points": current_user.total_points
    })



@app.route('/play_interactive_game')

@login_required
def play_interactive_game():
    return redirect(url_for('game_start'))

@app.route('/game/reset', methods=['POST'])
@login_required
def reset_game():
    current_user.last_completed_level = 0
    current_user.total_points = 0
    db.session.commit()
    log_user_activity(current_user.id, "reset_game_progress")
    return jsonify({"status": "success", "message": "Progresso reiniciado com sucesso!"})

@app.route('/admin')
@login_required
def admin():
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    return render_template('admin/index.html')

@app.route('/admin/lessons')
@login_required
def admin_lessons():
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    lessons = TextAudioLesson.query.all()
    return render_template('admin/lessons.html', lessons=lessons)

@app.route('/admin/games')
@login_required
def admin_games():
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    games = InteractiveGame.query.all()
    return render_template('admin/games.html', games=games)

@app.route('/admin/lessons/add', methods=['GET', 'POST'])
@login_required
def add_lesson():
    if current_user.id != 1:
        flash(get_t('admin_flash_unauthorized'), 'danger')
        return redirect(url_for('home'))
    form = LessonForm()
    if form.validate_on_submit():
        if not form.audio.data:
            flash(get_t('admin_flash_audio_required'), 'danger')
            return render_template('admin/lesson_form.html', form=form, title=get_t('admin_title_add_lesson'))

        # Save the audio file
        audio_filename = secure_filename(form.audio.data.filename)
        audio_path = os.path.join(app.root_path, 'static/audio', audio_filename)
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        form.audio.data.save(audio_path)

        # Save the text file
        text_filename = f"{os.path.splitext(audio_filename)[0]}.txt"
        text_path = os.path.join(app.root_path, 'static/doc', text_filename)
        os.makedirs(os.path.dirname(text_path), exist_ok=True)
        with open(text_path, 'w') as f:
            f.write(form.text.data)

        new_lesson = TextAudioLesson(
            title=form.title.data,
            text_content=form.text.data,
            audio_file_path=os.path.join('audio', audio_filename),
            target_language=form.target_language.data
        )
        db.session.add(new_lesson)
        db.session.commit()
        flash(get_t('admin_flash_lesson_added'), 'success')
        return redirect(url_for('admin_lessons'))
    return render_template('admin/lesson_form.html', form=form, title=get_t('admin_title_add_lesson'))

@app.route('/admin/lessons/edit/<int:lesson_id>', methods=['GET', 'POST'])
@login_required
def edit_lesson(lesson_id):
    if current_user.id != 1:
        flash(get_t('admin_flash_unauthorized'), 'danger')
        return redirect(url_for('home'))
    lesson = TextAudioLesson.query.get_or_404(lesson_id)
    form = LessonForm(obj=lesson)
    if form.validate_on_submit():
        lesson.title = form.title.data
        lesson.text_content = form.text.data
        lesson.target_language = form.target_language.data

        if form.audio.data:
            # Delete old audio file
            if lesson.audio_file_path:
                old_path = os.path.join(app.root_path, 'static', lesson.audio_file_path)
                if os.path.exists(old_path):
                    os.remove(old_path)
            # Save new audio file
            audio_filename = secure_filename(form.audio.data.filename)
            audio_path = os.path.join(app.root_path, 'static/audio', audio_filename)
            form.audio.data.save(audio_path)
            lesson.audio_file_path = os.path.join('audio', audio_filename)

        db.session.commit()
        flash(get_t('admin_flash_lesson_updated'), 'success')
        return redirect(url_for('admin_lessons'))
    return render_template('admin/lesson_form.html', form=form, title=get_t('admin_title_edit_lesson'))

@app.route('/admin/lessons/delete/<int:lesson_id>', methods=['POST'])
@login_required
def delete_lesson(lesson_id):
    if current_user.id != 1:
        flash(get_t('admin_flash_unauthorized'), 'danger')
        return redirect(url_for('home'))
    lesson = TextAudioLesson.query.get_or_404(lesson_id)
    # Delete audio file
    if lesson.audio_file_path:
        audio_path = os.path.join(app.root_path, 'static', lesson.audio_file_path)
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except OSError:
                pass
    # Delete text file
    if lesson.audio_file_path:
        text_filename = f"{os.path.splitext(os.path.basename(lesson.audio_file_path))[0]}.txt"
        text_path = os.path.join(app.root_path, 'static/doc', text_filename)
        if os.path.exists(text_path):
            try:
                os.remove(text_path)
            except OSError:
                pass
    db.session.delete(lesson)
    db.session.commit()
    flash(get_t('admin_flash_lesson_deleted'), 'success')
    return redirect(url_for('admin_lessons'))

@app.route('/admin/games/add', methods=['GET', 'POST'])
@login_required
def add_game():
    if current_user.id != 1:
        flash(get_t('admin_flash_unauthorized'), 'danger')
        return redirect(url_for('home'))
    form = GameForm()
    if form.validate_on_submit():
        if not form.image.data:
            flash(get_t('admin_flash_image_required'), 'danger')
            return render_template('admin/game_form.html', form=form, title=get_t('admin_title_add_game'))

        # Save the image file
        image_filename = secure_filename(form.image.data.filename)
        image_path = os.path.join(app.root_path, 'static/images/games', image_filename)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        form.image.data.save(image_path)

        new_game = InteractiveGame(
            level_id=form.level_id.data,
            level_title=form.level_title.data,
            image_file_path=os.path.join('games', image_filename),
            word=form.word.data,
            target_language=form.target_language.data
        )
        db.session.add(new_game)
        db.session.commit()
        flash(get_t('admin_flash_game_added'), 'success')
        return redirect(url_for('admin_games'))
    return render_template('admin/game_form.html', form=form, title=get_t('admin_title_add_game'))

@app.route('/admin/games/edit/<int:game_id>', methods=['GET', 'POST'])
@login_required
def edit_game(game_id):
    if current_user.id != 1:
        flash(get_t('admin_flash_unauthorized'), 'danger')
        return redirect(url_for('home'))
    game = InteractiveGame.query.get_or_404(game_id)
    form = GameForm()
    if form.validate_on_submit():
        game.level_id = form.level_id.data
        game.level_title = form.level_title.data
        game.word = form.word.data
        game.target_language = form.target_language.data

        if form.image.data:
            # Delete old image file
            if game.image_file_path:
                try:
                    os.remove(os.path.join(app.root_path, 'static/images', game.image_file_path))
                except OSError:
                    pass
            # Save new image file
            image_filename = secure_filename(form.image.data.filename)
            image_path = os.path.join(app.root_path, 'static/images/games', image_filename)
            form.image.data.save(image_path)
            game.image_file_path = os.path.join('games', image_filename)

        db.session.commit()
        flash(get_t('admin_flash_game_updated'), 'success')
        return redirect(url_for('admin_games'))
    elif request.method == 'GET':
        form.level_id.data = game.level_id
        form.level_title.data = game.level_title
        form.word.data = game.word
        form.target_language.data = game.target_language
    return render_template('admin/game_form.html', form=form, title=get_t('admin_title_edit_game'))


@app.route('/admin/games/delete/<int:game_id>', methods=['POST'])
@login_required
def delete_game(game_id):
    if current_user.id != 1:
        flash(get_t('admin_flash_unauthorized'), 'danger')
        return redirect(url_for('home'))
    game = InteractiveGame.query.get_or_404(game_id)
    # Delete image file
    if game.image_file_path:
        image_path = os.path.join(app.root_path, 'static/images', game.image_file_path)
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
            except OSError:
                pass
    db.session.delete(game)
    db.session.commit()
    flash(get_t('admin_flash_game_deleted'), 'success')
    return redirect(url_for('admin_games'))

@app.route('/debug-routes')
def debug_routes():
    output = []
    for rule in app.url_map.iter_rules():
        output.append(f"Endpoint: {rule.endpoint}, Methods: {rule.methods}, Rule: {rule.rule}")
    return "<br>".join(output)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True,port=5006)
