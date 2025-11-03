from app import app, db
from models import TextAudioLesson, InteractiveGame

with app.app_context():
    # Clear existing data (optional, for fresh start)
    db.session.query(TextAudioLesson).delete()
    db.session.query(InteractiveGame).delete()
    db.session.commit()

    # Add dummy TextAudioLesson data
    lesson1 = TextAudioLesson(
        title="Spanish Greetings",
        text_content="Hola, ¿cómo estás? Muy bien, gracias. ¿Y tú?",
        audio_file_path="videos/dummy_audio.mp3",
        target_language="Spanish"
    )
    lesson2 = TextAudioLesson(
        title="French Basics",
        text_content="Bonjour, comment ça va? Ça va bien, merci. Et toi?",
        audio_file_path="videos/dummy_audio.mp3",
        target_language="French"
    )
    db.session.add_all([lesson1, lesson2])

    # Add dummy InteractiveGame data
    game1 = InteractiveGame(
        title="Animals in Spanish",
        image_file_path="images/dummy_image.jpg",
        correct_word="Perro",
        incorrect_words="Gato,Pez,Pájaro",
        target_language="Spanish"
    )
    game2 = InteractiveGame(
        title="Fruits in French",
        image_file_path="images/dummy_image.jpg",
        correct_word="Pomme",
        incorrect_words="Banane,Orange,Fraise",
        target_language="French"
    )
    db.session.add_all([game1, game2])

    db.session.commit()
    print("Dummy data added successfully!")
