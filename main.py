from machine import Machine
from ui import UI
from player import Player
from settings import *
import buttons
import ctypes, pygame, sys
import tkinter as tk
import json

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH).convert_alpha()
        self.grid_image = pygame.image.load(GRID_IMAGE_PATH).convert_alpha()
        self.player = Player()
        self.machine = Machine(self.player)
        self.ui = UI(self.player)
        self.delta_time = 0

        # Sound
        pygame.mixer.music.load('audio/track.mp3')
        pygame.mixer.music.play(loops = -1)
        self.create_music_control_buttons()

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
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=4)

    def create_music_control_buttons(self):
        # Load the button images
        img_music_on = pygame.image.load('graphics/0/symbols/mun250.png').convert_alpha()
        img_music_off = pygame.image.load('graphics/0/symbols/muf250.png').convert_alpha()
        # Create the button widgets
        self.button_music_on = buttons.Button(1325, 930, img_music_on, 0.2)
        self.button_music_off = buttons.Button(1325, 930, img_music_off, 0.2)

        self.music_on = True

    def toggle_music(self):
        if self.music_on:
            pygame.mixer.music.pause()
            self.music_on = False
        else:
            pygame.mixer.music.unpause()
            self.music_on = True

    def show_menu_popup(self):
        # Create the popup window
        popup_window = tk.Tk()
        popup_window.geometry("300x200")
        popup_window.title("Menu")

        # Add some content to the window
        label = tk.Label(popup_window, text="This is the menu popup.")
        label.pack(pady=20)

        pygame.quit()
        sys.exit()

    def run(self):
        users = self.load_users()
        balance = self.load_balance()

        player_data = self.player.get_data()
        self.start_time = pygame.time.get_ticks()

        img_plus5 = pygame.image.load('graphics/0/symbols/plus5.png').convert_alpha()
        button_plus5 = buttons.Button(1500, 910, img_plus5, 0.1) 
        img_minus5 = pygame.image.load('graphics/0/symbols/minus5.png').convert_alpha()
        button_minus5 = buttons.Button(1450, 910, img_minus5, 0.1) 

        img_plus55 = pygame.image.load('graphics/0/symbols/plus5.png').convert_alpha()
        button_plus55 = buttons.Button(220, 910, img_plus5, 0.1) 
        img_minus55 = pygame.image.load('graphics/0/symbols/minus5.png').convert_alpha()
        button_minus55 = buttons.Button(280, 910, img_minus5, 0.1)

        img_menu = pygame.image.load('graphics/0/symbols/menu.png').convert_alpha()
        button_menu = buttons.Button(1250, 930, img_menu, 0.18)

        while True:
            player_data = self.player.get_data()

            if  button_plus5.draw(self.screen): 
                self.machine.changebetplus()
            if  button_minus5.draw(self.screen): 
                self.machine.changebetminus()
            if button_menu.draw(self.screen):
                users[balance[0]][1] = player_data['balance']
                self.save_users(users)
                self.show_menu_popup()

            if  button_plus55.draw(self.screen) and float(player_data['music_volume']) < 100: 
                self.player.chage_music_volume_plus()
            if  button_minus55.draw(self.screen) and float(player_data['music_volume']) > 0: 
                self.player.chage_music_volume_minus()

            # Handle music control
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.button_music_on.rect.collidepoint(pos):
                        self.toggle_music()
                    elif self.button_music_off.rect.collidepoint(pos):
                        self.toggle_music()
                
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.screen.blit(self.grid_image, (0, 0))

            # Show the music control buttons based on the music state
            if self.music_on:
                self.button_music_on.draw(self.screen)
            else:
                self.button_music_off.draw(self.screen)

            self.clock.tick(FPS)

            pygame.mixer.music.set_volume(float(player_data['music_volume']) / 100)

if __name__ == '__main__':
    game = Game()
    game.run()