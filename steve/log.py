import json
import os

LOG_PATH = "log_sent.json"

def load_log():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            return json.load(f)
    return {}

def save_log(log):
    with open(LOG_PATH, "w") as f:
        json.dump(log, f)

