from settings import *


class Player():
    def __init__(self):
        import json
        with open('balance.json') as json_file:
            data = json.load(json_file)

        self.balance = float(data[2])
        self.bet_size = 10.00
        self.last_payout = 0.00
        self.total_won = 0.00
        self.total_wager = 0.00
        self.last_loss = 0.00
        self.music_volume = 50.00
        self.xp = int(data[3])
        self.level = self.determine_level()
        self.free_spins = int(data[4])
        self.audio_track = data[5]
        self.audio_on = data[6]
        self.admin = data[7]
        self.banned = data[8]
    
    def get_data(self):
        player_data = {}
        player_data['balance'] = "{:.2f}".format(self.balance)
        player_data['bet_size'] = "{:.2f}".format(self.bet_size)
        player_data['last_payout'] = "{:.2f}".format(self.last_payout) if self.last_payout else "N/A"
        player_data['total_won'] = "{:.2f}".format(self.total_won)
        player_data['total_wager'] = "{:.2f}".format(self.total_wager)
        player_data['last_loss'] = "{:.2f}".format(self.last_loss) if self.last_loss else "N/A"
        player_data['music_volume'] = "{:.2f}".format(self.music_volume)
        player_data['xp'] = self.xp
        player_data['free_spins'] = self.free_spins
        player_data['audio_track'] = self.audio_track
        player_data['audio_on'] = self.audio_on
        player_data['admin'] = self.admin
        player_data['banned'] = self.banned
        return player_data

    def place_bet(self):
        bet = self.bet_size
        if self.free_spins == 0:
            self.balance -= bet
            self.total_wager += bet
            self.add_xp(bet)
        else:
            self.subtract_free_spins()


    def change_bet_plus(self):
        if  self.bet_size <= self.balance - 5.00:
            self.bet_size += 5.00
        
    def change_bet_minus(self):
        if  self.bet_size > 5.00:
            self.bet_size -= 5.00

    def chage_music_volume_plus(self):
        self.music_volume += 5

    def chage_music_volume_minus(self):
        self.music_volume -= 5

    def chage_balance_minus(self, value):
        self.balance -= value

    def change_balance_plus(self, value):
        self.balance += value

    def add_xp(self, value):
        self.xp += value
        self.add_free_spins()

    def determine_level(self):
        return int(self.xp / 100)

    def add_free_spins(self):
        if self.level < self.determine_level():
            self.level = self.determine_level()
            self.free_spins += 10

    def subtract_free_spins(self):
        self.free_spins -= 1

    def audio_track_change(self, track_path):
        self.audio_track = track_path

    def audio_on_of(self, state):
        self.audio_on = state