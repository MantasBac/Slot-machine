import shutil
import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import ttk
import pygame
from PIL import ImageTk, Image
import tkinter.font as tkfont
from data_save_load import Data

class Menu:
    def __init__(self, player):
        self.player = player
        self.popup_window = tk.Tk()
        self.data = Data(self.player)

        style = ttk.Style(self.popup_window)
        style.theme_create('combobox_black_background', parent='alt',
                           settings={'TCombobox': {'configure': {'fieldbackground': '#1e1e1e',
                                                                 'background': 'white',
                                                                 'foreground': 'white',
                                                                 'font': ('Times New Roman', 18)}}})

        style.theme_use('combobox_black_background')

    def show_menu_popup(self):
        # Create the popup window
        for widget in self.popup_window.winfo_children():
            widget.destroy()
        self.popup_window.title("Menu")
        self.popup_window.geometry("1048x524")
        self.popup_window.configure(bg='#1e1e1e')
        width, height = 256, 256

        image_settings = Image.open("graphics/0/symbols/settings.png")
        resized_image = image_settings.resize((width, height))
        photo_settings = ImageTk.PhotoImage(resized_image)

        image_help = Image.open("graphics/0/symbols/help.png")
        resized_image = image_help.resize((width, height))
        photo_help = ImageTk.PhotoImage(resized_image)

        image_info = Image.open("graphics/0/symbols/info.png")
        resized_image = image_info.resize((width, height))
        photo_info = ImageTk.PhotoImage(resized_image)

        image_deposit = Image.open("graphics/0/symbols/deposit.png")
        resized_image = image_deposit.resize((width, height))
        photo_deposit = ImageTk.PhotoImage(resized_image)

        image_withdraw = Image.open("graphics/0/symbols/withdraw.png")
        resized_image = image_withdraw.resize((width, height))
        photo_withdraw = ImageTk.PhotoImage(resized_image)

        image_stop= Image.open("graphics/0/symbols/stop.png")
        resized_image = image_stop.resize((width, height))
        photo_stop = ImageTk.PhotoImage(resized_image)


        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        image_admin = Image.open("graphics/0/symbols/ban.jpg")
        resized_image = image_admin.resize((width, height))
        photo_admin = ImageTk.PhotoImage(resized_image)

        image_stop = Image.open("graphics/0/symbols/stop.png")
        resized_image = image_stop.resize((width, height))
        photo_stop = ImageTk.PhotoImage(resized_image)

        button_settings = tk.Button(self.popup_window, image=photo_settings, bg='#1e1e1e', command=self.show_settings)
        button_help = tk.Button(self.popup_window, image=photo_help, bg='#1e1e1e', command=self.show_help)
        button_info = tk.Button(self.popup_window, image=photo_info, bg='#1e1e1e', command=self.show_info)
        button_deposit = tk.Button(self.popup_window, image=photo_deposit, bg='#1e1e1e', command=self.show_deposit)
        button_withdraw = tk.Button(self.popup_window, image=photo_withdraw, bg='#1e1e1e', command=self.show_withdraw)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('menu'))
        button_admin = tk.Button(self.popup_window, image=photo_admin, bg='#1e1e1e', command=self.show_admin)
        button_stop = tk.Button(self.popup_window, image=photo_stop, bg='#1e1e1e', command=self.delete_user)

        self.popup_window.columnconfigure(0, weight=0)

        button_settings.grid(row=0, column=0)
        button_help.grid(row=0, column=1)
        button_info.grid(row=0, column=2)
        button_deposit.grid(row=1, column=0)
        button_withdraw.grid(row=1, column=1)
        button_stop.grid(row=1, column=2)

        if self.player.admin:
            button_admin.grid(row=1, column=2)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()


    def block_user(self, acc):
        if str(self.data.load_balance[0]) ==acc:
            self.player.banned = True
            self.data.save()

    def delete_user(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        username_label = tk.Label(self.popup_window, text='Username: ', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=18, anchor='w')
        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_delete = tk.Button(self.popup_window, text='Delete', bg='#1e1e1e', fg='white', command= lambda: self.block_user(username_entry), font=('Times New Roman', 18))
        username_entry = tk.Entry(self.popup_window, font=('Times New Roman', 18))


        button_back.grid(row=0, column=0, sticky='W')
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        button_delete.grid(row=1, column=2)

        self.popup_window.mainloop()

    def show_settings(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Settings")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        selected_track = tk.StringVar()
        def track_selection(event):
            selected_value = selected_track.get()
            if selected_value == "Theme #1":
                music = "audio/track1.mp3"
            elif selected_value == "Theme #2":
                music = "audio/track2.mp3"
            elif selected_value == "Theme #3":
                music = "audio/track3.mp3"
            self.set_music(music, self.player.audio_on)
            self.show_settings()

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('settings'))

        if self.player.audio_track == "audio/track1.mp3":
            self.current = 0
        if self.player.audio_track == "audio/track2.mp3":
            self.current = 1
        if self.player.audio_track == "audio/track3.mp3":
            self.current = 2

        dropdown = ttk.Combobox(self.popup_window, textvariable=selected_track)
        dropdown["values"] = ("Theme #1", "Theme #2", "Theme #3")
        dropdown.current(self.current)
        dropdown.bind("<<ComboboxSelected>>", track_selection)
        font = tkfont.Font(family='Times New Roman', size=18)
        dropdown.configure(font=font)

        label_sound_track = tk.Label(self.popup_window, text="Selected track: ", bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))

        self.popup_window.columnconfigure(0, weight=0)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_sound_track.grid(row=1, column=0)
        dropdown.grid(row=1, column=1)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_help(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('help'))

        self.popup_window.columnconfigure(0, weight=0)

        button_back.grid(row=0, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

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

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_dev1 = tk.Button(self.popup_window, image=photo_dev1, bg='#1e1e1e', command=self.show_dev1)
        button_dev2 = tk.Button(self.popup_window, image=photo_dev2, bg='#1e1e1e', command=self.show_dev2)
        button_dev3 = tk.Button(self.popup_window, image=photo_dev3, bg='#1e1e1e', command=self.show_dev3)
        button_dev4 = tk.Button(self.popup_window, image=photo_dev4, bg='#1e1e1e', command=self.show_dev4)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('info'))

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

        self.popup_window.columnconfigure(0, weight=0)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_info.grid(row=1, column=0, columnspan=4)
        button_dev1.grid(row=2, column=0)
        button_dev2.grid(row=2, column=1)
        button_dev3.grid(row=2, column=2)
        button_dev4.grid(row=2, column=3)
        label_dev1.grid(row=3, column=0)
        label_dev2.grid(row=3, column=1)
        label_dev3.grid(row=3, column=2)
        label_dev4.grid(row=3, column=3)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_dev1(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_dev_music('audio/sr.mp3', self.player.audio_on)

        self.popup_window.title("Simonas Radžius")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/sr.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('dev1'))

        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Simonas Radžius', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Beisbolkių baryga', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 18))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_dev2(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_dev_music('audio/ap.mp3', self.player.audio_on)

        self.popup_window.title("Arnas Pilius")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/ap.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('dev2'))

        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Arnas Pilius', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Gariūnų viršininkas', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_dev3(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_dev_music('audio/gb.mp3', self.player.audio_on)

        self.popup_window.title("Gytis Baltrušaitis")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/gb.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('dev3'))

        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Gytis Baltrušaitis', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Top G', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_dev4(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.set_dev_music('audio/mb.mp3', self.player.audio_on)

        self.popup_window.title("Mantas Bačinskas")
        width, height = 256, 256

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_dev = Image.open("graphics/developer_pictures/mb.jpg")
        resized_image = image_dev.resize((width, height))
        photo_dev = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_info)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('dev4'))

        label_img_dev = tk.Label(self.popup_window, image=photo_dev, bg='#1e1e1e')
        label_dev = tk.Label(self.popup_window, text='Mantas Bačinskas', bg='#1e1e1e', fg='white',
                             font=('Times New Roman', 20))

        label_empty = tk.Label(self.popup_window, text='', font=('Times New Roman', 20))

        label_prof = tk.Label(self.popup_window, text='Profesija: Marozas', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_deposit(self):
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

        self.popup_window.columnconfigure(0, weight=0)

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

    def show_admin(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('admin'))

        self.popup_window.columnconfigure(0, weight=0)

        button_back.grid(row=0, column=0, sticky=tk.W)

        users = self.data.load_users()
        i = 0
        for user in users:
            if users[user][6] == False and users[user][7] == True:
                button_user_ban = tk.Button(self.popup_window, text='UNBAN', command=lambda acc=user: self.ban(acc))
            elif users[user][6] == False and users[user][7] == False:
                button_user_ban = tk.Button(self.popup_window, text='BAN', command=lambda acc=user: self.ban(acc))
            else:
                button_user_ban = tk.Label(self.popup_window, text='ADMIN', bg='#1e1e1e', fg='white',
                                    font=('Times New Roman', 18))
            label_user = tk.Label(self.popup_window, text=str((i+1)) + '. ' + user + ': ', bg='#1e1e1e', fg='white',
                                    font=('Times New Roman', 18))
            label_user.grid(row=i+1, column=0, sticky='W')
            button_user_ban.grid(row=i+1, column=1, sticky='E')
            i += 1

        i = 0
        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def ban(self, user):
        users = self.data.load_users()

        if users[user][7] == True:
            users[user][7] = False
            print('unbanned')
        else:
            users[user][7] = True
            print('banned')

        self.data.save_users(users)
        self.show_admin()

    def set_music(self, path, state):
        self.player.audio_track = path
        self.data.save()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=-1)
        if not state:
            pygame.mixer.music.pause()

    def set_dev_music(self, path, state):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=-1)
        if not state:
            pygame.mixer.music.pause()

    def change_sound(self, window):
        if self.player.audio_on:
            pygame.mixer.music.pause()
            self.player.audio_on = False
            if window == 'menu':
                self.show_menu_popup()
            elif window == 'settings':
                self.show_settings()
            elif window == 'help':
                self.show_help()
            elif window == 'info':
                self.show_info()
            elif window == 'dev1':
                self.show_dev1()
            elif window == 'dev2':
                self.show_dev2()
            elif window == 'dev3':
                self.show_dev3()
            elif window == 'dev4':
                self.show_dev4()
            elif window == 'admin':
                self.show_admin()
        else:
            pygame.mixer.music.unpause()
            self.player.audio_on = True
            if window == 'menu':
                self.show_menu_popup()
            elif window == 'settings':
                self.show_settings()
            elif window == 'help':
                self.show_help()
            elif window == 'info':
                self.show_info()
            elif window == 'dev1':
                self.show_dev1()
            elif window == 'dev2':
                self.show_dev2()
            elif window == 'dev3':
                self.show_dev3()
            elif window == 'dev4':
                self.show_dev4()
            elif window == 'admin':
                self.show_admin()