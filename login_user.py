import tkinter as tk
import json
import main
import time
import os
from settings import *

# create a file to store the registered users
entry = False

# function to load users from file
def load_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def load_balance():
    try:
        with open(BALANCE_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# function to save users to file
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def save_balance(balances):
    with open(BALANCE_FILE, 'w') as f:
        json.dump(balances, f)

# create a dictionary of registered users
users = load_users()
balances = load_balance()
# function to check if user exists and password is correct
def login():
    global entry
    username = username_entry.get()
    password = password_entry.get()
    if (username == ''):
        message_label.config(text='Username field is empty')
    elif (password == ''):
        message_label.config(text='Password field is empty')
    elif username in users and users[username][0] == password:
        message_label.config(text='Login successful!')

        #balances = users[username][1]
        balances = [username, users[username][0], users[username][1], users[username][2], users[username][3]]
        save_balance(balances)
        entry = True
        return entry
    else:
        message_label.config(text='Invalid username or password. Please sign up.')
        entry = False
        return entry


# function to create a new user and return to login page
def signup():
    username = new_username_entry.get()
    password = new_password_entry.get()
    balance = balance_add_entry.get()
    if (username == ''):
        sign_up_message_label.config(text='Username field is empty')
    elif (password == ''):
        sign_up_message_label.config(text='Password field is empty')
    elif (balance == ''):
        sign_up_message_label.config(text='Balance field is empty')
    else:
        users[username] = [password, balance, 100, 0]
        save_users(users)
        signup_frame.pack_forget()
        login_frame.pack()

def enter():
    if entry == True:
        root.destroy()
        os.system('python main.py')
    else:
        print("NOPE")

# create the GUI
root = tk.Tk()
root.title('Sign in')
root.geometry('1000x600')
root.configure(bg='#1e1e1e')

# create the login frame
login_frame = tk.Frame(root)
login_frame.configure(bg='#1e1e1e')
login_frame.pack(fill='both', expand=True)

# create the blank space before logo lable
space_before = tk.Label(login_frame, text='', bg='#1e1e1e', font=('Times New Roman', 18))
space_before.pack()

# create the logo lable
logo_label = tk.Label(login_frame, text='SLOTS', bg='#1e1e1e', fg='white', font=('Arial', 36), width=18)
logo_label.pack()

# create the blank space after logo lable
space_after = tk.Label(login_frame, text='', bg='#1e1e1e', font=('Times New Roman', 36))
space_after.pack()

# create the username label and entry
username_label = tk.Label(login_frame, text='Username:', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=18, anchor='w')
username_label.pack()
username_entry = tk.Entry(login_frame, font=('Times New Roman', 18))
username_entry.pack()

# create the password label and entry
password_label = tk.Label(login_frame, text='Password:', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=18, anchor='w')
password_label.pack()
password_entry = tk.Entry(login_frame, show='*', font=('Times New Roman', 18))
password_entry.pack()

# create the blank space between buttons
space = tk.Label(login_frame, text='', bg='#1e1e1e', font=('Times New Roman', 18), width=18, anchor='w')
space.pack()

# create the login button
login_button = tk.Button(login_frame, text='Login', command=login, bg='#292929', fg='white', width=12, font=('Arial', 16))
login_button.pack()

# create the message label
message_label = tk.Label(login_frame, text='', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=100)
message_label.pack()

# create the sign-up frame
signup_frame = tk.Frame(root)
signup_frame.configure(bg='#1e1e1e')

# create the blank space before logo lable
space_before1 = tk.Label(signup_frame, text='', bg='#1e1e1e', font=('Times New Roman', 18))
space_before1.pack()

# create the logo lable
logo_label1 = tk.Label(signup_frame, text='SLOTS', bg='#1e1e1e', fg='white', font=('Arial', 36), width=18)
logo_label1.pack()

# create the blank space after logo lable
space_after1 = tk.Label(signup_frame, text='', bg='#1e1e1e', font=('Times New Roman', 36))
space_after1.pack()

# create the new username label and entry
new_username_label = tk.Label(signup_frame, text='New username:', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=18, anchor='w')
new_username_label.pack()
new_username_entry = tk.Entry(signup_frame, font=('Times New Roman', 18))
new_username_entry.pack()

# create the new password label and entry
new_password_label = tk.Label(signup_frame, text='New password:', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=18, anchor='w')
new_password_label.pack()
new_password_entry = tk.Entry(signup_frame, show='*', font=('Times New Roman', 18))
new_password_entry.pack()

# create the balance add label and entry
balance_add_label = tk.Label(signup_frame, text='Balance:', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=18, anchor='w')
balance_add_label.pack()
balance_add_entry = tk.Entry(signup_frame, font=('Times New Roman', 18))
balance_add_entry.pack()

# create the blank space before buttons
space = tk.Label(signup_frame, text='', bg='#1e1e1e', font=('Times New Roman', 18), width=18, anchor='w')
space.pack()

# create the sign-up button
signup_button = tk.Button(signup_frame, text='Sign up', command=signup, bg='#292929', fg='white', width=12, font=('Arial', 16))
signup_button.pack()

# create the message label
sign_up_message_label = tk.Label(signup_frame, text='', bg='#1e1e1e', fg='white', font=('Times New Roman', 18), width=100)
sign_up_message_label.pack()

# create the back button
back_button = tk.Button(signup_frame, text='Back', command=lambda: signup_frame.pack_forget() or login_frame.pack(), bg='#292929', fg='white', width=12, font=('Arial', 16))
back_button.pack()

# create the login/enter button
enter_button = tk.Button(login_frame, text='Enter', command=enter, bg='#292929', fg='white', width=12, font=('Arial', 16))  ##, command=login
enter_button.pack()

# create the sign-up button
signup_nav_button = tk.Button(login_frame, text='Sign up', command=lambda: login_frame.pack_forget() or signup_frame.pack(), bg='#292929', fg='white', width=12, font=('Arial', 16))
signup_nav_button.pack()

# run the GUI
root.mainloop()