import shutil
import subprocess
import tkinter as tk
from pathlib import Path

import pygame
from PIL import ImageTk, Image

class Menu:
    def __init__(self, player):
        self.player = player
        self.popup_window = tk.Tk()

    def show_menu_popup(self):
        # Create the popup window
        for widget in self.popup_window.winfo_children():
            widget.destroy()
        self.popup_window.title("Menu")
        self.popup_window.geometry("1048x600")
        self.popup_window.configure(bg='#1e1e1e')
        width, height = 256, 256

        image_settings = Image.open("graphics/0/symbols/settings.png")
        resized_image = image_settings.resize((width, height))
        photo_settings = ImageTk.PhotoImage(resized_image)

        image_info = Image.open("graphics/0/symbols/info.png")
        resized_image = image_info.resize((width, height))
        photo_info = ImageTk.PhotoImage(resized_image)

        image_help = Image.open("graphics/0/symbols/help.png")
        resized_image = image_help.resize((width, height))
        photo_help = ImageTk.PhotoImage(resized_image)

        image_deposit = Image.open("graphics/0/symbols/deposit.png")
        resized_image = image_deposit.resize((width, height))
        photo_deposit = ImageTk.PhotoImage(resized_image)

        image_withdraw = Image.open("graphics/0/symbols/withdraw.png")
        resized_image = image_withdraw.resize((width, height))
        photo_withdraw = ImageTk.PhotoImage(resized_image)

        button_settings = tk.Button(self.popup_window, image=photo_settings, bg='#1e1e1e', command=self.show_settings)
        button_info = tk.Button(self.popup_window, image=photo_info, bg='#1e1e1e', command=self.show_info)
        button_help = tk.Button(self.popup_window, image=photo_help, bg='#1e1e1e', command=self.show_help)
        button_deposit = tk.Button(self.popup_window, image=photo_deposit, bg='#1e1e1e', command=self.show_deposit)
        button_withdraw = tk.Button(self.popup_window, image=photo_withdraw, bg='#1e1e1e', command=self.show_withdraw)

        button_settings.grid(row=0, column=0)
        button_info.grid(row=0, column=1)
        button_help.grid(row=0, column=2)
        button_deposit.grid(row=1, column=0)
        button_withdraw.grid(row=1, column=1)

        self.popup_window.mainloop()

    def show_settings(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Settings")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)

        button_back.grid(row=1, column=0, sticky=tk.W)

        self.popup_window.mainloop()

    def show_deposit(self):
        print('deposit')

    def show_help(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)

        button_back.grid(row=1, column=0, sticky=tk.W)

        self.popup_window.mainloop()

    def show_withdraw(self):
        print('withdraw')

    def show_info(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Settings")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev1 = Image.open("graphics/developer_pictures/sr.jpg")
        resized_image = image_dev1.resize((width, height))
        photo_dev1 = ImageTk.PhotoImage(resized_image)

        image_dev2 = Image.open("graphics/developer_pictures/ap.jpg")
        resized_image = image_dev2.resize((width, height))
        photo_dev2 = ImageTk.PhotoImage(resized_image)

        image_dev3 = Image.open("graphics/developer_pictures/gb.jpg")
        resized_image = image_dev3.resize((width, height))
        photo_dev3 = ImageTk.PhotoImage(resized_image)

        image_dev4 = Image.open("graphics/developer_pictures/mb.jpg")
        resized_image = image_dev4.resize((width, height))
        photo_dev4 = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_dev1 = tk.Button(self.popup_window, image=photo_dev1, bg='#1e1e1e', command=self.show_dev1)
        button_dev2 = tk.Button(self.popup_window, image=photo_dev2, bg='#1e1e1e', command=self.show_dev2)
        button_dev3 = tk.Button(self.popup_window, image=photo_dev3, bg='#1e1e1e', command=self.show_dev3)
        button_dev4 = tk.Button(self.popup_window, image=photo_dev4, bg='#1e1e1e', command=self.show_dev4)

        label_info = tk.Label(self.popup_window, text='Informacija apie kūrėjus', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 32), pady=10)
        label_dev1 = tk.Label(self.popup_window, text='Simonas Radžius', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 18))
        label_dev2 = tk.Label(self.popup_window, text='Arnas Pilius', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 18))
        label_dev3 = tk.Label(self.popup_window, text='Gytis Baltrušaitis', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))
        label_dev4 = tk.Label(self.popup_window, text='Mantas Bačinskas', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 18))

        button_back.grid(row=1, column=0, sticky=tk.W)
        label_info.grid(row=2, column=0, columnspan=4)
        button_dev1.grid(row=3, column=0)
        button_dev2.grid(row=3, column=1)
        button_dev3.grid(row=3, column=2)
        button_dev4.grid(row=3, column=3)
        label_dev1.grid(row=4, column=0)
        label_dev2.grid(row=4, column=1)
        label_dev3.grid(row=4, column=2)
        label_dev4.grid(row=4, column=3)

        self.popup_window.mainloop()

    def show_dev1(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_music('audio/sr.mp3')

        self.popup_window.title("Simonas Radžius")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/sr.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Simonas Radžius', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Beisbolkių baryga', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 18))

        button_back.grid(row=1, column=0, sticky=tk.W)
        label_img_dev.grid(row=2, column=0, columnspan=4)
        label_dev.grid(row=3, column=0, columnspan=4)
        label_empty.grid(row=4, column=0, columnspan=2)
        label_prof.grid(row=6, column=0, sticky=tk.W)



        self.popup_window.columnconfigure(0, weight=1)

        self.popup_window.mainloop()

    def show_dev2(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_music('audio/ap.mp3')

        self.popup_window.title("Arnas Pilius")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/ap.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Arnas Pilius', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Gariūnų viršininkas', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))

        button_back.grid(row=1, column=0, sticky=tk.W)
        label_img_dev.grid(row=2, column=0, columnspan=4)
        label_dev.grid(row=3, column=0, columnspan=4)
        label_empty.grid(row=4, column=0, columnspan=2)
        label_prof.grid(row=6, column=0, sticky=tk.W)

        self.popup_window.columnconfigure(0, weight=1)

        self.popup_window.mainloop()

    def show_dev3(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_music('audio/gb.mp3')

        self.popup_window.title("Gytis Baltrušaitis")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/gb.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Gytis Baltrušaitis', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Top G', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))

        button_back.grid(row=1, column=0, sticky=tk.W)
        label_img_dev.grid(row=2, column=0, columnspan=4)
        label_dev.grid(row=3, column=0, columnspan=4)
        label_empty.grid(row=4, column=0, columnspan=2)
        label_prof.grid(row=6, column=0, sticky=tk.W)

        self.popup_window.columnconfigure(0, weight=1)

        self.popup_window.mainloop()

    def show_dev4(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_music('audio/mb.mp3')

        self.popup_window.title("Mantas Bačinskas")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/mb.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Mantas Bačinskas', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Marozas', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))

        button_back.grid(row=1, column=0, sticky=tk.W)
        label_img_dev.grid(row=2, column=0, columnspan=4)
        label_dev.grid(row=3, column=0, columnspan=4)
        label_empty.grid(row=4, column=0, columnspan=2)
        label_prof.grid(row=6, column=0, sticky=tk.W)

        self.popup_window.columnconfigure(0, weight=1)

        self.popup_window.mainloop()

    def show_withdraw(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Withdraw")
        self.popup_window.geometry("1050x334")
        self.popup_window.configure(bg='#1e1e1e')
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

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
            if (num == 0):
                file_path = "graphics/withdraw_rewards/0.jpg"
            elif (num == 1):
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

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button = tk.Button(self.popup_window, image=photo, command=button_click)
        button1 = tk.Button(self.popup_window, image=photo1, command=button_click1)
        button2 = tk.Button(self.popup_window, image=photo2, command=button_click2)
        button3 = tk.Button(self.popup_window, image=photo3, command=button_click3)

        label_kaina = tk.Label(self.popup_window, text='Kaina: 300', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))
        label_kaina1 = tk.Label(self.popup_window, text='Kaina: 150', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))
        label_kaina2 = tk.Label(self.popup_window, text='Kaina: 50', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))
        label_kaina3 = tk.Label(self.popup_window, text='Kaina: 10', bg='#1e1e1e', fg='white', font=('Times New Roman', 18))

        button_back.grid(row=0, column=0, sticky=tk.W)
        button.grid(row=1, column=0)
        label_kaina.grid(row=2, column=0)
        button1.grid(row=1, column=1)
        label_kaina1.grid(row=2, column=1)
        button2.grid(row=1, column=2)
        label_kaina2.grid(row=2, column=2)
        button3.grid(row=1, column=3)
        label_kaina3.grid(row=2, column=3)

        self.popup_window.mainloop()

    def set_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=-1)