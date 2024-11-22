# Installation
### Clone the repository:

bash
Copier le code
git clone https://github.com/your-username/interchange.git
cd interchange
Set up a virtual environment:

<<<<<<< HEAD
`bash`
=======
bash
>>>>>>> e24f64bc82e51468053ab9ad5b6668d3094028bd
Copier le code
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies:

<<<<<<< HEAD
`bash`
Copier le code
`pip install -r requirements.txt`
Set up environment variables:

Create a `.env` file in the root directory with the following variables:
=======
bash
Copier le code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory with the following variables:
>>>>>>> e24f64bc82e51468053ab9ad5b6668d3094028bd

plaintext
Copier le code
SECRET_KEY=your-secure-secret-key  # Replace with a strong secret key
DATABASE_URL=postgresql://username:password@localhost/interchange  # Update with your PostgreSQL credentials
Set up the database:

bash
Copier le code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the application:

bash
Copier le code
flask run --port=5001
The app will be available at http://127.0.0.1:5001.

Usage
Register for a new account or log in with an existing one.
Update your profile with details such as native language, learning language, and interests.
Create flashcards to help memorize vocabulary and language structures.
Post in the forum to interact with other users and engage in language discussions.
File Structure
app.py: Main application file, initializes Flask app and extensions, defines routes.
models.py: Contains database models (User, Flashcard, ForumPost).
forms.py: Contains WTForms for user registration, login, profile update, etc.
templates/: Jinja2 templates for rendering pages (e.g., home.html, register.html, dashboard.html).
static/: Folder for static assets (e.g., CSS, JavaScript, images).
Security
This app includes several security measures:

CSRF Protection: Protects forms from CSRF attacks.
Rate Limiting: Limits requests per user to prevent abuse.
Talisman: Sets up security headers.
Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/new-feature).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a pull request.
License
<<<<<<< HEAD
This project is licensed under the MIT License.
=======
This project is licensed under the MIT License.
