import json
import os
from datetime import datetime

def _history_file(username):
    return f"history_{username}.json"

def save_game_history(username, game_title):
    if not username:
        return
    file = _history_file(username)
    data = json.load(open(file)) if os.path.exists(file) else []

    if game_title not in [g["title"] for g in data]:
        data.append({
            "title": game_title,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    json.dump(data, open(file, "w"), indent=2)

def load_game_history(username):
    file = _history_file(username)
    return json.load(open(file)) if os.path.exists(file) else []

def clear_game_history(username):
    file = _history_file(username)
    if os.path.exists(file):
        os.remove(file)