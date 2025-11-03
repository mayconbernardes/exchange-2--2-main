# Installation
### Clone the repository:

bash
Copier le code
git clone https://github.com/your-username/interchange.git
cd interchange
Set up a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Set up environment variables:

Create a `.env` file in the root directory with the following variables:

```plaintext
Copier le code
SECRET_KEY=your-secure-secret-key  # Replace with a strong secret key
DATABASE_URL=postgresql://username:password@localhost/bdName  # Update with your PostgreSQL credentials
Set up the database:

bash
Copier le code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the application:

```bash
flask run --port=5001
```
The app will be available at http://127.0.0.1:5001.

## Running with Docker

To run the application using Docker Compose (recommended for development and deployment):

1.  **Build and run the containers:**

    ```bash
    docker-compose up --build
    ```

    This will build the Flask application image, start the PostgreSQL database, and run the Flask app. The Flask app will automatically run database migrations.

2.  **Access the application:**

    The app will be available at `http://localhost:5006`.

3.  **Stop the containers:**

    ```bash
    docker-compose down
    ```

Usage
Register for a new account or log in with an existing one.
Update your profile with details such as native language, learning language, and interests.
Create flashcards to help memorize vocabulary and language structures.
Learn languages with texts and audio, using transcriptions to improve comprehension.
Engage in interactive games by matching images with their correct word names.
File Structure
app.py: Main application file, initializes Flask app and extensions, defines routes.
models.py: Contains database models (User, Flashcard, TextAudioLesson, InteractiveGame).
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
This project is licensed under the MIT License.
