from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    native_language = db.Column(db.String(50), nullable=True)
    learning_language = db.Column(db.String(50), nullable=True)
    profile_picture = db.Column(db.String(200), nullable=True)
    interests = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_completed_level = db.Column(db.Integer, default=0)
    total_points = db.Column(db.Integer, default=0)
    is_admin = db.Column(db.Boolean, default=False)

    def get_id(self):
        return str(self.id)  # Required for Flask-Login to load user

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('flashcards', lazy=True))


class TextAudioLesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text_content = db.Column(db.Text, nullable=False)
    audio_file_path = db.Column(db.String(255), nullable=False)
    target_language = db.Column(db.String(50), nullable=False)

class InteractiveGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, nullable=True)
    level_title = db.Column(db.String(100), nullable=True)
    image_file_path = db.Column(db.String(255), nullable=False)
    word = db.Column(db.String(100), nullable=True)
    target_language = db.Column(db.String(50), nullable=True)