import shutil
import subprocess
import sys
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

        if not self.player.admin:
            button_stop.grid(row=1, column=2)

        if self.player.admin:
            button_admin.grid(row=1, column=2)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def block_user(self, acc):
        balance = self.data.load_balance()
        print('deletinu')
        print(balance[0])
        if balance[0] == acc:
            self.player.banned = True
            self.data.save()
            pygame.quit()
            sys.exit()

    def delete_user(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        username_label = tk.Label(self.popup_window, text='Username: ', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=18, anchor='w')
        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_delete = tk.Button(self.popup_window, text='Delete', bg='#1e1e1e', fg='white', command= lambda: self.block_user(username_entry.get()), font=('Times New Roman', 18))
        username_entry = tk.Entry(self.popup_window, font=('Times New Roman', 18))

        button_back.grid(row=0, column=0, sticky='W')
        username_label.grid(row=1, column=0, sticky='W')
        username_entry.grid(row=1, column=1, sticky='W')
        button_delete.grid(row=1, column=2, sticky='E')

        self.popup_window.mainloop()

    def show_settings(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Settings")
        self.popup_window.geometry("1048x524")
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

        self.popup_window.title("Help")
        self.popup_window.geometry("1048x764")
        width, height = 32, 32

        image_back = Image.open("graphics/0/symbols/back.png")
        resized_image = image_back.resize((32, 32))
        photo_back = ImageTk.PhotoImage(resized_image)

        image_green = Image.open("graphics/0/symbols/0_diamond.png")
        resized_image = image_green.resize((width, height))
        photo_green = ImageTk.PhotoImage(resized_image)

        image_purple = Image.open("graphics/0/symbols/0_floppy.png")
        resized_image = image_purple.resize((width, height))
        photo_purple = ImageTk.PhotoImage(resized_image)

        image_red = Image.open("graphics/0/symbols/0_hourglass.png")
        resized_image = image_red.resize((width, height))
        photo_red = ImageTk.PhotoImage(resized_image)

        image_pink = Image.open("graphics/0/symbols/0_telephone.png")
        resized_image = image_pink.resize((width, height))
        photo_pink = ImageTk.PhotoImage(resized_image)

        if self.player.audio_on:
            self.image_sound = Image.open('graphics/0/symbols/mun250.png')
        else:
            self.image_sound = Image.open('graphics/0/symbols/muf250.png')
        resized_image = self.image_sound.resize((50, 50))
        photo_sound = ImageTk.PhotoImage(resized_image)

        button_back = tk.Button(self.popup_window, image=photo_back, bg='#1e1e1e', command=self.show_menu_popup)
        button_sound = tk.Button(self.popup_window, image=photo_sound, bg='#1e1e1e',
                                 command=lambda: self.change_sound('help'))

        label_green = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green1 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green2 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green_3 = tk.Label(self.popup_window, text='  -  27 (x2.7)', bg='#1e1e1e', fg='white',
                               font=('Times New Roman', 24), pady=10)

        label_green3 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green4 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green5 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green6 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green_4 = tk.Label(self.popup_window, text='  -  36 (x3.6)', bg='#1e1e1e', fg='#66fa66',
                                 font=('Times New Roman', 24), pady=10)

        label_green7 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green8 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green9 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green10 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green11 = tk.Label(self.popup_window, image=photo_green, bg='#1e1e1e')
        label_green_5 = tk.Label(self.popup_window, text='  -  45 (x4.5)', bg='#1e1e1e', fg='#13fa02',
                                 font=('Times New Roman', 24), pady=10)

        label_purple = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple1 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple2 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple_3 = tk.Label(self.popup_window, text='  -  18 (x1.8)', bg='#1e1e1e', fg='white',
                               font=('Times New Roman', 24), pady=10)

        label_purple3 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple4 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple5 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple6 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple_4 = tk.Label(self.popup_window, text='  -  24 (x2.4)', bg='#1e1e1e', fg='#5f4187',
                                 font=('Times New Roman', 24), pady=10)

        label_purple7 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple8 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple9 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple10 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple11 = tk.Label(self.popup_window, image=photo_purple, bg='#1e1e1e')
        label_purple_5 = tk.Label(self.popup_window, text='  -  30 (x3.0)', bg='#1e1e1e', fg='#4e02c9',
                                  font=('Times New Roman', 24), pady=10)

        label_red = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red1 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red2 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red_3 = tk.Label(self.popup_window, text='  -  15 (x1.5)', bg='#1e1e1e', fg='white',
                               font=('Times New Roman', 24), pady=10)

        label_red3 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red4 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red5 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red6 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red_4 = tk.Label(self.popup_window, text='  -  20 (x2.0)', bg='#1e1e1e', fg='#874144',
                              font=('Times New Roman', 24), pady=10)

        label_red7 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red8 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red9 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red10 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red11 = tk.Label(self.popup_window, image=photo_red, bg='#1e1e1e')
        label_red_5 = tk.Label(self.popup_window, text='  -  25 (x2.5)', bg='#1e1e1e', fg='#ed0202',
                                  font=('Times New Roman', 24), pady=10)

        label_pink = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink1 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink2 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink_3 = tk.Label(self.popup_window, text='  -  15 (x1.5)', bg='#1e1e1e', fg='white',
                                  font=('Times New Roman', 24), pady=10)

        label_pink3 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink4 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink5 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink6 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink_4 = tk.Label(self.popup_window, text='  -  20 (x2.0)', bg='#1e1e1e', fg='#874184',
                                font=('Times New Roman', 24), pady=10)

        label_pink7 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink8 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink9 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink10 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink11 = tk.Label(self.popup_window, image=photo_pink, bg='#1e1e1e')
        label_pink_5 = tk.Label(self.popup_window, text='  -  25 (x2.5)', bg='#1e1e1e', fg='#ed02be',
                                font=('Times New Roman', 24), pady=10)

        self.popup_window.columnconfigure(0, weight=0)

        button_back.grid(row=0, column=0, sticky=tk.W)

        label_green.grid(row=1, column=0)
        label_green1.grid(row=1, column=1)
        label_green2.grid(row=1, column=2)
        label_green_3.grid(row=1, column=5, sticky='E')

        label_green3.grid(row=2, column=0)
        label_green4.grid(row=2, column=1)
        label_green5.grid(row=2, column=2)
        label_green6.grid(row=2, column=3)
        label_green_4.grid(row=2, column=5, sticky='E')

        label_green7.grid(row=3, column=0)
        label_green8.grid(row=3, column=1)
        label_green9.grid(row=3, column=2)
        label_green10.grid(row=3, column=3)
        label_green11.grid(row=3, column=4)
        label_green_5.grid(row=3, column=5, sticky='E')

        label_purple.grid(row=4, column=0)
        label_purple1.grid(row=4, column=1)
        label_purple2.grid(row=4, column=2)
        label_purple_3.grid(row=4, column=5, sticky='E')

        label_purple3.grid(row=5, column=0)
        label_purple4.grid(row=5, column=1)
        label_purple5.grid(row=5, column=2)
        label_purple6.grid(row=5, column=3)
        label_purple_4.grid(row=5, column=5, sticky='E')

        label_purple7.grid(row=6, column=0)
        label_purple8.grid(row=6, column=1)
        label_purple9.grid(row=6, column=2)
        label_purple10.grid(row=6, column=3)
        label_purple11.grid(row=6, column=4)
        label_purple_5.grid(row=6, column=5, sticky='E')

        label_red.grid(row=7, column=0)
        label_red1.grid(row=7, column=1)
        label_red2.grid(row=7, column=2)
        label_red_3.grid(row=7, column=5, sticky='E')

        label_red3.grid(row=8, column=0)
        label_red4.grid(row=8, column=1)
        label_red5.grid(row=8, column=2)
        label_red6.grid(row=8, column=3)
        label_red_4.grid(row=8, column=5, sticky='E')

        label_red7.grid(row=9, column=0)
        label_red8.grid(row=9, column=1)
        label_red9.grid(row=9, column=2)
        label_red10.grid(row=9, column=3)
        label_red11.grid(row=9, column=4)
        label_red_5.grid(row=9, column=5, sticky='E')

        label_pink.grid(row=10, column=0)
        label_pink1.grid(row=10, column=1)
        label_pink2.grid(row=10, column=2)
        label_pink_3.grid(row=10, column=5, sticky='E')

        label_pink3.grid(row=11, column=0)
        label_pink4.grid(row=11, column=1)
        label_pink5.grid(row=11, column=2)
        label_pink6.grid(row=11, column=3)
        label_pink_4.grid(row=11, column=5, sticky='E')

        label_pink7.grid(row=12, column=0)
        label_pink8.grid(row=12, column=1)
        label_pink9.grid(row=12, column=2)
        label_pink10.grid(row=12, column=3)
        label_pink11.grid(row=12, column=4)
        label_pink_5.grid(row=12, column=5, sticky='E')

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_info(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Info apie kūrėjus")
        self.popup_window.geometry("1048x524")
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

        self.popup_window.title("Simonas Radžius")
        self.popup_window.geometry("1048x564")

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
        label_about1 = tk.Label(self.popup_window, text='Daugiausiai prisidėta prie:', bg='#1e1e1e', fg='white',
                              font=('Times New Roman', 18))
        label_about2 = tk.Label(self.popup_window, text='  --Aministratoriaus/žaidėjo paskyrų logika, duomenų saugojimas', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))
        label_about3 = tk.Label(self.popup_window, text='  --Muzikos logika', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))
        label_about4 = tk.Label(self.popup_window, text='  --Pinigų išgryninimo logika', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)
        label_about1.grid(row=6, column=0, sticky=tk.W)
        label_about2.grid(row=7, column=0, sticky=tk.W)
        label_about3.grid(row=8, column=0, sticky=tk.W)
        label_about4.grid(row=9, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_dev2(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Arnas Pilius")
        self.popup_window.geometry("1048x564")

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
        label_about1 = tk.Label(self.popup_window, text='Daugiausiai prisidėta prie:', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 18))
        label_about2 = tk.Label(self.popup_window,
                                text='  --Prisijungimo sistema', bg='#1e1e1e',
                                fg='white',
                                font=('Times New Roman', 14))
        label_about3 = tk.Label(self.popup_window, text='  --Žaidėjo savęs blokavimo sistema', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)
        label_about1.grid(row=6, column=0, sticky=tk.W)
        label_about2.grid(row=7, column=0, sticky=tk.W)
        label_about3.grid(row=8, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_dev3(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Gytis Baltrušaitis")
        self.popup_window.geometry("1048x564")

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
        label_about1 = tk.Label(self.popup_window, text='Daugiausiai prisidėta prie:', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 18))
        label_about2 = tk.Label(self.popup_window,
                                text='  --Automato logikos karkasas', bg='#1e1e1e',
                                fg='white',
                                font=('Times New Roman', 14))
        label_about3 = tk.Label(self.popup_window, text='  --Didžioji dalis grafinio dizaino', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))
        label_about4 = tk.Label(self.popup_window, text='  --Laimėjimų logika', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)
        label_about1.grid(row=6, column=0, sticky=tk.W)
        label_about2.grid(row=7, column=0, sticky=tk.W)
        label_about3.grid(row=8, column=0, sticky=tk.W)
        label_about4.grid(row=9, column=0, sticky=tk.W)

        button_sound.place(relx=1, rely=1, anchor="se")

        self.popup_window.mainloop()

    def show_dev4(self):
        for widget in self.popup_window.winfo_children():
            widget.destroy()

        self.popup_window.title("Mantas Bačinskas")
        self.popup_window.geometry("1048x564")

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
        label_about1 = tk.Label(self.popup_window, text='Daugiausiai prisidėta prie:', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 18))
        label_about2 = tk.Label(self.popup_window,
                                text='  --Automato logikos karkasas', bg='#1e1e1e',
                                fg='white',
                                font=('Times New Roman', 14))
        label_about3 = tk.Label(self.popup_window, text='  --Pinigų įdėjimo logika', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))
        label_about4 = tk.Label(self.popup_window, text='  --Statymo sistema', bg='#1e1e1e', fg='white',
                                font=('Times New Roman', 14))

        self.popup_window.columnconfigure(0, weight=1)

        button_back.grid(row=0, column=0, sticky=tk.W)
        label_img_dev.grid(row=1, column=0, columnspan=4)
        label_dev.grid(row=2, column=0, columnspan=4)
        label_empty.grid(row=3, column=0, columnspan=2)
        label_prof.grid(row=5, column=0, sticky=tk.W)
        label_about1.grid(row=6, column=0, sticky=tk.W)
        label_about2.grid(row=7, column=0, sticky=tk.W)
        label_about3.grid(row=8, column=0, sticky=tk.W)
        label_about4.grid(row=9, column=0, sticky=tk.W)

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

        self.popup_window.title("Admin menu")
        self.popup_window.geometry("1048x524")

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