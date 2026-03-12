import json

class DatasetManager:

    def save_battle(self, data):

        with open("data/battle_log.json", "a") as f:
            f.write(json.dumps(data) + "\n")