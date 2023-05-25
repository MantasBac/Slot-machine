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
    
    def get_data(self):
        #import login_user
        #from login_user import balance
        #login_user.root.destroy()
        
        player_data = {}
        player_data['balance'] = "{:.2f}".format(float(self.balance))
        player_data['bet_size'] = "{:.2f}".format(self.bet_size)
        player_data['last_payout'] = "{:.2f}".format(self.last_payout) if self.last_payout else "N/A"
        player_data['total_won'] = "{:.2f}".format(self.total_won)
        player_data['total_wager'] = "{:.2f}".format(self.total_wager)
        player_data['last_loss'] = "{:.2f}".format(self.last_loss) if self.last_loss else "N/A"
        player_data['music_volume'] = "{:.2f}".format(self.music_volume)
        return player_data

    def place_bet(self):
        bet = self.bet_size
        self.balance -= bet
        self.total_wager += bet

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