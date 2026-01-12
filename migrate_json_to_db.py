import json
import os
from app import app, db
from models import InteractiveGame

def migrate_game_data():
    with app.app_context():
        # Clear existing game data to avoid duplicates during migration
        InteractiveGame.query.delete()
        
        try:
            with open('data/levels.json', 'r') as f:
                levels_data = json.load(f)
            
            for level in levels_data['levels']:
                level_id = level['id']
                level_title = level['title']
                for item in level['items']:
                    new_game_item = InteractiveGame(
                        level_id=level_id,
                        level_title=level_title,
                        image_file_path=item['image'],
                        word=item['word'],
                        target_language='en'  # Default for existing data
                    )
                    db.session.add(new_game_item)
            
            db.session.commit()
            print("Successfully migrated game data from JSON to Database.")
        except FileNotFoundError:
            print("levels.json not found. Skipping migration.")
        except Exception as e:
            print(f"Error migrating game data: {e}")

if __name__ == '__main__':
    migrate_game_data()
