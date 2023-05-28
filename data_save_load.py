import json
import os
import shutil
from settings import *

class Data:
    def __init__(self, Player):
        self.player = Player

    def load_balance(self):
        try:
            with open(BALANCE_FILE, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    # function to load users from file
    def load_users(self):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    # function to save users to file
    def save_users(self, users):
        shutil.copyfile(USERS_FILE, BACKUP_FILE)

        try:
            with open(USERS_FILE + '.tmp', 'w') as f:
                json.dump(users, f, indent=4)

            os.replace(USERS_FILE + '.tmp', USERS_FILE)

            if os.path.exists(BACKUP_FILE):
                os.remove(BACKUP_FILE)

        except Exception as e:
            # An error occurred, restore the backup file if it exists
            if os.path.exists(BACKUP_FILE):
                shutil.copyfile(BACKUP_FILE, USERS_FILE)

            print(f"An error occurred while saving the users: {str(e)}")

    def save(self):
        users = self.load_users()
        balance = self.load_balance()
        users[balance[0]][1] = self.player.balance
        users[balance[0]][2] = self.player.xp
        users[balance[0]][3] = self.player.free_spins
        users[balance[0]][4] = self.player.audio_track
        users[balance[0]][5] = self.player.audio_on
        users[balance[0]][7] = self.player.banned
        self.save_users(users)