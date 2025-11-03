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
from forms import UserProfileForm, FlashcardForm, LoginForm, RegistrationForm  # Ensure these forms are in forms.py

# Initialize Flask app
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_very_secret_key')  # Use environment variable or a default
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://root:root@localhost/interchange')  # Use environment variable or a default
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # Limit of 1 MB for uploads

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
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
socketio = SocketIO(app)
Talisman(app, content_security_policy=None)
Session(app)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)  # Add remember functionality here
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.native_language = form.native_language.data
        current_user.learning_language = form.learning_language.data
        current_user.interests = form.interests.data
        
        if form.profile_picture.data:
            filename = secure_filename(form.profile_picture.data.filename)
            images_dir = os.path.join(app.root_path, 'static', 'images')
            os.makedirs(images_dir, exist_ok=True)
            picture_path = os.path.join(images_dir, filename)
            form.profile_picture.data.save(picture_path)
            current_user.profile_picture = filename
        
        db.session.commit()
        flash('Your profile has been updated.', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.native_language.data = current_user.native_language
        form.learning_language.data = current_user.learning_language
        form.interests.data = current_user.interests
    return render_template('profile.html', form=form)

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
        return redirect(url_for('flashcards'))
    
    user_flashcards = Flashcard.query.filter_by(user_id=current_user.id).all()
    return render_template('flashcard.html', form=form, flashcards=user_flashcards)

@app.route('/user/<int:user_id>')
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)  # Fetch user by ID
    return render_template('user_profile.html', user=user)  # Render user profile template

@app.route('/learn_text_audio')
def learn_text_audio():
    # Caminho absoluto para o arquivo de transcrição
    transcription_path = os.path.join(app.static_folder, 'doc', 'introducingYourFriends.txt')

    # Debug: imprime o caminho absoluto para verificar
    print(f"Procurando transcrição em: {os.path.abspath(transcription_path)}")

    try:
        # Lê o arquivo com codificação UTF-8 (ou outra se necessário)
        with open(transcription_path, 'r', encoding='utf-8') as file:
            transcription = file.read()
        print("Transcrição carregada com sucesso!")
    except FileNotFoundError as e:
        transcription = f"""
        <div style="color: #ff0000; padding: 10px; background-color: #fff0f0; border-radius: 5px;">
            <strong>Erro:</strong> Arquivo de transcrição não encontrado em: {os.path.abspath(transcription_path)}
            <br><br>
            Verifique se:
            <ul>
                <li>O arquivo existe no caminho correto</li>
                <li>O nome do arquivo está escrito corretamente (incluindo maiúsculas/minúsculas)</li>
                <li>O arquivo tem permissões de leitura</li>
            </ul>
            <br>
            Mensagem de erro: {str(e)}
        </div>
        """
    except Exception as e:
        transcription = f"""
        <div style="color: #ff0000; padding: 10px; background-color: #fff0f0; border-radius: 5px;">
            <strong>Erro inesperado ao ler a transcrição:</strong> {str(e)}
        </div>
        """

    return render_template('learn_text_audio.html', transcription=transcription)


@app.route('/game')
def game_start():
    return redirect(url_for('game_level', level_id=1))

@app.route('/game/<int:level_id>')
def game_level(level_id):
    try:
        with open('data/levels.json', 'r') as f:
            levels_data = json.load(f)
        
        total_levels = len(levels_data['levels'])
        level = next((lvl for lvl in levels_data['levels'] if lvl['id'] == level_id), None)
        
        if not level:
            flash('Level not found.', 'danger')
            return redirect(url_for('dashboard'))

        # Shuffle items for the game
        game_items = level['items']
        random.shuffle(game_items)
        
        # Extract words and shuffle them
        words = [item['word'] for item in game_items]
        random.shuffle(words)
        
        return render_template(
            'interactive_game.html', 
            level=level, 
            game_items=game_items, 
            words=words,
            level_id=level_id,
            total_levels=total_levels
        )

    except FileNotFoundError:
        flash('Game data not found.', 'danger')
        return redirect(url_for('dashboard'))
    except (json.JSONDecodeError, KeyError):
        flash('Invalid game data format.', 'danger')
        return redirect(url_for('dashboard'))


@app.route('/play_interactive_game')
@login_required
def play_interactive_game():
    return redirect(url_for('game_start'))

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
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    form = LessonForm()
    if form.validate_on_submit():
        # Save the audio file
        audio_filename = secure_filename(form.audio.data.filename)
        audio_path = os.path.join(app.root_path, 'static/audio', audio_filename)
        form.audio.data.save(audio_path)

        # Save the text file
        text_filename = f"{os.path.splitext(audio_filename)[0]}.txt"
        text_path = os.path.join(app.root_path, 'static/doc', text_filename)
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
        flash('Lesson added successfully!', 'success')
        return redirect(url_for('admin_lessons'))
    return render_template('admin/lesson_form.html', form=form, title='Add Lesson')

@app.route('/admin/lessons/edit/<int:lesson_id>', methods=['GET', 'POST'])
@login_required
def edit_lesson(lesson_id):
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
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
                os.remove(os.path.join(app.root_path, 'static', lesson.audio_file_path))
            # Save new audio file
            audio_filename = secure_filename(form.audio.data.filename)
            audio_path = os.path.join(app.root_path, 'static/audio', audio_filename)
            form.audio.data.save(audio_path)
            lesson.audio_file_path = os.path.join('audio', audio_filename)

        db.session.commit()
        flash('Lesson updated successfully!', 'success')
        return redirect(url_for('admin_lessons'))
    return render_template('admin/lesson_form.html', form=form, title='Edit Lesson')

@app.route('/admin/lessons/delete/<int:lesson_id>', methods=['POST'])
@login_required
def delete_lesson(lesson_id):
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    lesson = TextAudioLesson.query.get_or_404(lesson_id)
    # Delete audio file
    if lesson.audio_file_path:
        os.remove(os.path.join(app.root_path, 'static', lesson.audio_file_path))
    # Delete text file
    text_filename = f"{os.path.splitext(os.path.basename(lesson.audio_file_path))[0]}.txt"
    text_path = os.path.join(app.root_path, 'static/doc', text_filename)
    if os.path.exists(text_path):
        os.remove(text_path)
    db.session.delete(lesson)
    db.session.commit()
    flash('Lesson deleted successfully!', 'success')
    return redirect(url_for('admin_lessons'))

@app.route('/admin/games/add', methods=['GET', 'POST'])
@login_required
def add_game():
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    form = GameForm()
    if form.validate_on_submit():
        # Save the image file
        image_filename = secure_filename(form.image.data.filename)
        image_path = os.path.join(app.root_path, 'static/images', image_filename)
        form.image.data.save(image_path)

        new_game = InteractiveGame(
            title=form.title.data,
            image_file_path=os.path.join('images', image_filename),
            correct_word=form.correct_word.data,
            incorrect_words=form.incorrect_words.data,
            target_language=form.target_language.data
        )
        db.session.add(new_game)
        db.session.commit()
        flash('Game added successfully!', 'success')
        return redirect(url_for('admin_games'))
    return render_template('admin/game_form.html', form=form, title='Add Game')

@app.route('/admin/games/edit/<int:game_id>', methods=['GET', 'POST'])
@login_required
def edit_game(game_id):
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    game = InteractiveGame.query.get_or_404(game_id)
    form = GameForm(obj=game)
    if form.validate_on_submit():
        game.title = form.title.data
        game.correct_word = form.correct_word.data
        game.incorrect_words = form.incorrect_words.data
        game.target_language = form.target_language.data

        if form.image.data:
            # Delete old image file
            if game.image_file_path:
                os.remove(os.path.join(app.root_path, 'static', game.image_file_path))
            # Save new image file
            image_filename = secure_filename(form.image.data.filename)
            image_path = os.path.join(app.root_path, 'static/images', image_filename)
            form.image.data.save(image_path)
            game.image_file_path = os.path.join('images', image_filename)

        db.session.commit()
        flash('Game updated successfully!', 'success')
        return redirect(url_for('admin_games'))
    return render_template('admin/game_form.html', form=form, title='Edit Game')

@app.route('/admin/games/delete/<int:game_id>', methods=['POST'])
@login_required
def delete_game(game_id):
    if current_user.id != 1:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('home'))
    game = InteractiveGame.query.get_or_404(game_id)
    # Delete image file
    if game.image_file_path:
        os.remove(os.path.join(app.root_path, 'static', game.image_file_path))
    db.session.delete(game)
    db.session.commit()
    flash('Game deleted successfully!', 'success')
    return redirect(url_for('admin_games'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True,port=5006)
