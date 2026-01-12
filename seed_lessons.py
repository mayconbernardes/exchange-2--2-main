from app import app, db
from models import TextAudioLesson

def seed_lessons():
    with app.app_context():
        # Check if any lessons exist
        if TextAudioLesson.query.count() == 0:
            lesson = TextAudioLesson(
                title="Introducing Your Friends",
                text_content="""
                <p>Hello! This is a simple transcription of the audio lesson.</p>
                <p>Learning how to introduce friends is a basic and essential skill.</p>
                """,
                audio_file_path="audio/introducingYourFriends.mp3",
                target_language="en"
            )
            db.session.add(lesson)
            db.session.commit()
            print("Added initial lesson to database.")
        else:
            print("Lessons already exist in database.")

if __name__ == '__main__':
    seed_lessons()
