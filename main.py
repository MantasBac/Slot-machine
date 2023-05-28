import shutil
from pathlib import Path
from machine import Machine
from ui import UI
from player import Player
from menu import Menu
from settings import *
from data_save_load import Data
import buttons
import ctypes, pygame, sys
import tkinter as tk
from PIL import ImageTk, Image
import subprocess

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
        self.data = Data(self.player)

        self.set_music(self.player.audio_track, self.player.audio_on)
        self.create_music_control_buttons(self.player.audio_on)

    def set_music(self, path, state):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=-1)
        if not state:
            pygame.mixer.music.pause()

    def create_music_control_buttons(self, state):
        # Load the button images
        img_music_on = pygame.image.load('graphics/0/symbols/mun250.png').convert_alpha()
        img_music_off = pygame.image.load('graphics/0/symbols/muf250.png').convert_alpha()
        # Create the button widgets
        self.button_music_on = buttons.Button(1325, 930, img_music_on, 0.2)
        self.button_music_off = buttons.Button(1325, 930, img_music_off, 0.2)

    def toggle_music(self):
        if self.player.audio_on:
            pygame.mixer.music.pause()
            self.player.audio_on = False

        else:
            pygame.mixer.music.unpause()
            self.player.audio_on = True

    def deposit(self):
        popup_window = tk.Tk()
        popup_window.title("Deposit")
        popup_window.geometry("1050x600")
        popup_window.configure(bg='#1e1e1e')

        def validate_card():
            card_number = card_entry.get()
            expiration_date = date_entry.get()
            cv_number = cv_entry.get()
            deposit_amount = deposit_entry.get()

            if card_number.strip() == "" or expiration_date.strip() == "" or cv_number.strip() == "" or deposit_amount.strip() == "":
                message_label.config(text='Please fill in all the fields!')
            elif not card_number.isdigit() or not expiration_date.isdigit() or not cv_number.isdigit() or not deposit_amount.isdigit():
                message_label.config(text='Please enter numbers only!')
            elif len(card_number) != 16 or len(expiration_date) != 4 or len(cv_number) != 3:
                message_label.config(text='Invalid card information!')
            else:
                message_label.config(text='Success, card information is valid!')
                self.player.change_balance_plus(float(deposit_amount))
                popup_window.after(1500, popup_window.destroy)

        card_label = tk.Label(popup_window, text="Card Number:", bg='#1e1e1e', fg='white', font=('Times New Roman', 20))
        card_label.place(x=100, y=50)
        card_entry = tk.Entry(popup_window, font=('Times New Roman', 20))
        card_entry.place(x=100, y=100)

        # Create a label and entry for expiration date
        date_label = tk.Label(popup_window, text="Expiration Date (MMYY):", bg='#1e1e1e', fg='white', font=('Times New Roman', 20))
        date_label.place(x=600, y=50)
        date_entry = tk.Entry(popup_window, font=('Times New Roman', 20))
        date_entry.place(x=600, y=100)

        # Create a label and entry for CV number
        cv_label = tk.Label(popup_window, text="CV Number:", bg='#1e1e1e', fg='white', font=('Times New Roman', 20))
        cv_label.place(x=100, y=200)
        cv_entry = tk.Entry(popup_window, font=('Times New Roman', 20))
        cv_entry.place(x=100, y=250)

        # Create a label and entry for deposit amount
        deposit_label = tk.Label(popup_window, text="Deposit Amount (in euros):", bg='#1e1e1e', fg='white', font=('Times New Roman', 20))
        deposit_label.place(x=100, y=400)
        deposit_entry = tk.Entry(popup_window, font=('Times New Roman', 20))
        deposit_entry.place(x=100, y=450)

        # Create a button to validate the card information and deposit amount
        validate_button = tk.Button(popup_window, text="Confirm deposit", bg='#1e1e1e', fg='white', font=('Times New Roman', 20), command=validate_card)
        validate_button.place(x=600, y=435)

        message_label = tk.Label(popup_window, text='', bg='#1e1e1e', fg='white', font=('Times New Roman', 20))
        message_label.place(x=600, y=250)

        popup_window.mainloop()

    def withdraw(self):
        popup_window = tk.Tk()
        popup_window.title("Withdraw")
        popup_window.geometry("1050x300")
        popup_window.configure(bg='#1e1e1e')
        width, height = 256, 256

        image = Image.open("graphics/withdraw_rewards/0.jpg")  # Replace with the path to your image file
        resized_image = image.resize((width, height))
        photo = ImageTk.PhotoImage(resized_image)

        image1 = Image.open("graphics/withdraw_rewards/1.jpg")  # Replace with the path to your image file
        resized_image = image1.resize((width, height))
        photo1 = ImageTk.PhotoImage(resized_image)

        image2 = Image.open("graphics/withdraw_rewards/2.jpg")  # Replace with the path to your image file
        resized_image = image2.resize((width, height))
        photo2 = ImageTk.PhotoImage(resized_image)

        image3 = Image.open("graphics/withdraw_rewards/3.jpg")  # Replace with the path to your image file
        resized_image = image3.resize((width, height))
        photo3 = ImageTk.PhotoImage(resized_image)

        def button_click():
            download_image(0)
            self.player.chage_balance_minus(300)

        def button_click1():
            download_image(1)
            self.player.chage_balance_minus(150)

        def button_click2():
            download_image(2)
            self.player.chage_balance_minus(50)

        def button_click3():
            download_image(3)
            self.player.chage_balance_minus(10)

        def download_image(num):
            # Prompt the user to select an image file
            if(num == 0):
                file_path = "graphics/withdraw_rewards/0.jpg"
            elif(num == 1):
                file_path = "graphics/withdraw_rewards/1.jpg"
            elif (num == 2):
                file_path = "graphics/withdraw_rewards/2.jpg"
            elif (num == 3):
                file_path = "graphics/withdraw_rewards/3.jpg"

            downloads_folder = Path.home() / "Downloads"
            destination_path = downloads_folder / Path(file_path).name

            shutil.copy(file_path, destination_path)

            # Open the Downloads folder with the downloaded image selected
            subprocess.Popen(['explorer', '/select,', str(destination_path)])

        button = tk.Button(popup_window, image=photo, command=button_click)
        button1 = tk.Button(popup_window, image=photo1, command=button_click1)
        button2 = tk.Button(popup_window, image=photo2, command=button_click2)
        button3 = tk.Button(popup_window, image=photo3, command=button_click3)

        label_kaina = tk.Label(popup_window, text='Kaina: 300', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))
        label_kaina1 = tk.Label(popup_window, text='Kaina: 150', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))
        label_kaina2 = tk.Label(popup_window, text='Kaina: 50', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))
        label_kaina3 = tk.Label(popup_window, text='Kaina: 10', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))

        button.grid(row=0, column=0)
        label_kaina.grid(row=1, column=0)
        button1.grid(row=0, column=1)
        label_kaina1.grid(row=1, column=1)
        button2.grid(row=0, column=2)
        label_kaina2.grid(row=1, column=2)
        button3.grid(row=0, column=3)
        label_kaina3.grid(row=1, column=3)

        popup_window.mainloop()

    def acc_banned(self):
        popup_window = tk.Tk()
        popup_window.title("Withdraw")
        popup_window.geometry("650x220")
        popup_window.configure(bg='#1e1e1e')
        width, height = 256, 211

        def disable_close():
            pass

        popup_window.protocol("WM_DELETE_WINDOW", disable_close)

        image_banned = Image.open("graphics/0/symbols/skull.png")
        resized_image = image_banned.resize((width, height))
        photo_banned = ImageTk.PhotoImage(resized_image)

        label_banned = tk.Label(popup_window, text='Your account has been banned', bg='#1e1e1e', fg='white',
                               font=('Times New Roman', 24))
        label_img_banned = tk.Label(popup_window, image=photo_banned, bg='#1e1e1e')

        label_banned.grid(row=0, column=0)
        label_img_banned.grid(row=0, column=1)

        popup_window.mainloop()

    def run(self):
        users = self.data.load_users()
        balance = self.data.load_balance()

        self.start_time = pygame.time.get_ticks()
        self.display_surface = pygame.display.get_surface()

        if self.player.banned == True:
            pygame.mixer.music.load('audio/banned.mp3')
            pygame.mixer.music.play(1)
            self.acc_banned()

        img_plus5 = pygame.image.load('graphics/0/symbols/plus5.png').convert_alpha()
        button_plus5 = buttons.Button(1500, 910, img_plus5, 0.1)
        img_minus5 = pygame.image.load('graphics/0/symbols/minus5.png').convert_alpha()
        button_minus5 = buttons.Button(1450, 910, img_minus5, 0.1)

        img_plus55 = pygame.image.load('graphics/0/symbols/plus5.png').convert_alpha()
        button_plus55 = buttons.Button(220, 910, img_plus5, 0.1)
        img_minus55 = pygame.image.load('graphics/0/symbols/minus5.png').convert_alpha()
        button_minus55 = buttons.Button(280, 910, img_minus5, 0.1)

        img_settings = pygame.image.load('graphics/0/symbols/menu.png').convert_alpha()
        button_settings = buttons.Button(1250, 930, img_settings, 0.18)

        img_deposit = pygame.image.load('graphics/0/symbols/deposit.png').convert_alpha()
        x, y = 340, self.display_surface.get_size()[1] - 90
        button_deposit = buttons.Button(x, y, img_deposit, 0.18)

        img_withdraw = pygame.image.load('graphics/0/symbols/withdraw.png').convert_alpha()
        x, y = 400, self.display_surface.get_size()[1] - 90
        button_withdraw = buttons.Button(x, y, img_withdraw, 0.18)
        
        while True:
            player_data = self.player.get_data()

            if  button_plus5.draw(self.screen): 
                self.machine.changebetplus()
            if  button_minus5.draw(self.screen): 
                self.machine.changebetminus()
            if  button_plus55.draw(self.screen) and float(player_data['music_volume']) < 100: 
                self.player.chage_music_volume_plus()
            if  button_minus55.draw(self.screen) and float(player_data['music_volume']) > 0: 
                self.player.chage_music_volume_minus()
            if button_settings.draw(self.screen):
                menu = Menu(self.player)
                menu.show_menu_popup()
            if button_deposit.draw(self.screen):
                self.deposit()
            if button_withdraw.draw(self.screen):
                self.withdraw()

            # Handle music control
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.button_music_on.rect.collidepoint(pos):
                        self.toggle_music()
                        self.data.save()
                    elif self.button_music_off.rect.collidepoint(pos):
                        self.toggle_music()
                        self.data.save()

            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data.save()
                    pygame.quit()
                    sys.exit()

            # Handle quit operation
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.screen.blit(self.grid_image, (0, 0))

            # Show the music control buttons based on the music state
            if self.player.audio_on:
                self.button_music_on.draw(self.screen)
            else:
                self.button_music_off.draw(self.screen)

            self.clock.tick(FPS)

            pygame.mixer.music.set_volume(float(player_data['music_volume']) / 100)

if __name__ == '__main__':
    game = Game()
    game.run()