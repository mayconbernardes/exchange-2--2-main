# app.py
import os

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request, session
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
from models import User, Flashcard, ForumPost  # Ensure these models are in models.py
from forms import UserProfileForm, FlashcardForm, LoginForm, RegistrationForm, ForumPostForm  # Ensure these forms are in forms.py

# Initialize Flask app
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = 'KJHY8!65LM@kLMQ#'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/interchange'  # Update for your environment
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # Limit of 1 MB for uploads

# Initialize extensions
db = SQLAlchemy(app)
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

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    native_language = db.Column(db.String(50))
    learning_language = db.Column(db.String(50))
    interests = db.Column(db.String(500))
    flashcards = db.relationship('Flashcard', backref='user', lazy=True)
    posts = db.relationship('ForumPost', backref='author', lazy=True)
    profile_picture = db.Column(db.String(255))  # Stores profile picture filename

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    translation = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

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

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    profile_form = UserProfileForm()
    flashcard_form = FlashcardForm()
    
    if request.method == 'POST':
        if 'update_profile' in request.form:
            if profile_form.validate_on_submit():
                current_user.username = profile_form.username.data
                current_user.native_language = profile_form.native_language.data
                current_user.learning_language = profile_form.learning_language.data
                current_user.interests = profile_form.interests.data
                
                if profile_form.profile_picture.data:
                    filename = secure_filename(profile_form.profile_picture.data.filename)
                    images_dir = os.path.join(app.root_path, 'static', 'images')
                    os.makedirs(images_dir, exist_ok=True)
                    picture_path = os.path.join(images_dir, filename)
                    profile_form.profile_picture.data.save(picture_path)
                    current_user.profile_picture = filename
                
                db.session.commit()
                flash('Your profile has been updated.', 'success')
                return redirect(url_for('dashboard'))
        
        elif 'create_flashcard' in request.form and flashcard_form.validate_on_submit():
            new_flashcard = Flashcard(
                word=flashcard_form.front.data,
                translation=flashcard_form.back.data,
                user_id=current_user.id
            )
            db.session.add(new_flashcard)
            db.session.commit()
            flash('Flashcard created successfully!', 'success')
            return redirect(url_for('dashboard'))
    
    elif request.method == 'GET':
        profile_form.username.data = current_user.username
        profile_form.native_language.data = current_user.native_language
        profile_form.learning_language.data = current_user.learning_language
        profile_form.interests.data = current_user.interests
    
    return render_template('dashboard.html', profile_form=profile_form, flashcard_form=flashcard_form)

@app.route('/forum')
def forum():
    # Fetch all users except the current user
    users = User.query.filter(User.id != current_user.id).all()  # Fetch all users except the logged-in user
    posts = ForumPost.query.order_by(ForumPost.date_posted.desc()).all()
    return render_template('forum.html', posts=posts, users=users)  # Pass users to the template

@app.route('/forum/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = ForumPostForm()
    if form.validate_on_submit():
        post = ForumPost(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('forum'))
    return render_template('create_post.html', form=form)

@app.route('/user/<int:user_id>')
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)  # Fetch user by ID
    return render_template('user_profile.html', user=user)  # Render user profile template

@app.route('/post/<int:post_id>')
def post(post_id):
    # Your logic to retrieve and display the post based on post_id
    return render_template('post.html', post_id=post_id)

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])  # Different route
def edit_post(post_id):
    # Logic for editing a post
    return render_template('edit_post.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True,port=5001)
    