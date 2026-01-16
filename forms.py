from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, FileField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from models import User

from flask_wtf.file import FileAllowed
from wtforms.widgets import ListWidget, CheckboxInput

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('de', 'German'),
    ('zh', 'Chinese'),
    ('hi', 'Hindi'),
    ('ar', 'Arabic'),
    ('pt', 'Portuguese'),
    ('ru', 'Russian'),
    ('ja', 'Japanese'),
    ('ko', 'Korean'),
    ('it', 'Italian'),
    ('nl', 'Dutch'),
    ('sv', 'Swedish'),
    ('no', 'Norwegian'),
    ('da', 'Danish'),
    ('fi', 'Finnish'),
    ('tr', 'Turkish'),
    ('pl', 'Polish'),
    ('th', 'Thai'),
    ('vi', 'Vietnamese'),
    ('id', 'Indonesian'),
    ('ms', 'Malay'),
    ('he', 'Hebrew'),
    ('el', 'Greek'),
    ('hu', 'Hungarian'),
    ('cs', 'Czech'),
    ('sk', 'Slovak'),
    ('ro', 'Romanian'),
    ('bg', 'Bulgarian'),
    ('hr', 'Croatian'),
    ('sr', 'Serbian'),
    ('uk', 'Ukrainian'),
    ('fa', 'Persian'),
    ('ur', 'Urdu'),
    ('bn', 'Bengali'),
    ('gu', 'Gujarati'),
    ('ta', 'Tamil'),
    ('te', 'Telugu'),
    ('mr', 'Marathi'),
    ('pa', 'Punjabi'),
    ('ml', 'Malayalam'),
    ('kn', 'Kannada'),
    ('my', 'Burmese'),
    ('km', 'Khmer'),
    ('lo', 'Lao'),
    ('ka', 'Georgian'),
    ('am', 'Amharic')
]

INTERESTS = [
    ('reading', 'Reading'),
    ('travel', 'Travel'),
    ('cooking', 'Cooking'),
    ('sports', 'Sports'),
    ('movies', 'Movies'),
    ('music', 'Music'),
    ('gaming', 'Gaming'),
    ('hiking', 'Hiking'),
    ('photography', 'Photography'),
    ('art', 'Art'),
    ('technology', 'Technology'),
    ('science', 'Science'),
    ('history', 'History'),
    ('politics', 'Politics'),
    ('fashion', 'Fashion'),
    ('writing', 'Writing'),
    ('gardening', 'Gardening'),
    ('pets', 'Pets'),
    ('volunteering', 'Volunteering'),
    ('learning_new_languages', 'Learning New Languages')
]

class UserProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64)])
    native_language = SelectField('Native Language', choices=LANGUAGES, validators=[DataRequired()])
    learning_language = SelectField('Learning Language', choices=LANGUAGES, validators=[DataRequired()])
    interests_selection = SelectMultipleField('Select Interests', choices=INTERESTS, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    interests = TextAreaField('Other Interests', validators=[Length(max=500)])
    profile_picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    description = TextAreaField('Description')
    submit = SubmitField('Update Profile')

class FlashcardForm(FlaskForm):
    front = StringField('Front', validators=[DataRequired()])
    back = StringField('Back', validators=[DataRequired()])
    submit = SubmitField('Create Flashcard')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  # Added remember checkbox
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long.'),
        Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
               message='Password must contain at least one uppercase letter, one lowercase letter, one number and one special character.')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered. Please choose a different one.')


class LessonForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    audio = FileField('Audio', validators=[FileAllowed(['mp3'], 'MP3 files only!')])
    target_language = SelectField('Target Language', choices=LANGUAGES, validators=[DataRequired()])
    submit = SubmitField('Submit')


class GameForm(FlaskForm):
    level_id = SelectField('Level', choices=[(str(i), f'Level {i}') for i in range(1, 11)], validators=[DataRequired()], coerce=int)
    level_title = StringField('Level Title', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    word = StringField('Word', validators=[DataRequired()])
    target_language = SelectField('Target Language', choices=LANGUAGES, validators=[DataRequired()])
    submit = SubmitField('Submit')



