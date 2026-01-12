@app.route('/game/complete/<int:level_id>', methods=['POST'])
@login_required
def complete_level(level_id):
    if level_id > current_user.last_completed_level:
        current_user.last_completed_level = level_id
        db.session.commit()
        log_user_activity(current_user.id, "completed_game_level", {"level_id": level_id})
    return jsonify({"status": "success", "last_completed_level": current_user.last_completed_level})
