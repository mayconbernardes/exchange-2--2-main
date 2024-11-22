from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    native_language = db.Column(db.String(50), nullable=False)
    learning_language = db.Column(db.String(50), nullable=False)
    profile_pic = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        return str(self.id)  # Required for Flask-Login to load user

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('flashcards', lazy=True))

class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"ForumPost('{self.title}', '{self.date_posted}')"

print("ForumPost model attributes:", ForumPost.__dict__)

# Modèle de la relation d'amitié entre utilisateurs
class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_1 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Premier utilisateur
    user_id_2 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Second utilisateur
    status = db.Column(db.String(20), default='pending')  # Statut de la demande (en attente, accepté, refusé)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Date de création de la relation d'amitié

    user_1 = db.relationship('User', foreign_keys=[user_id_1], backref='friendships_1', lazy=True)
    user_2 = db.relationship('User', foreign_keys=[user_id_2], backref='friendships_2', lazy=True)

# Modèle de message entre utilisateurs
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Utilisateur qui envoie le message
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Utilisateur qui reçoit le message
    content = db.Column(db.Text, nullable=False)  # Contenu du message
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Date et heure d'envoi du message
    read_status = db.Column(db.String(20), default='unread')  # Statut de lecture du message (lu ou non lu)

    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages', lazy=True)
    receiver = db.relationship('User', foreign_keys=[receiver_id], backref='received_messages', lazy=True)

