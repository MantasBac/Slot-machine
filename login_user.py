import tkinter as tk

# create a dictionary of registered users
users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}

# function to check if user exists and password is correct
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        message_label.config(text='Login successful!')
    else:
        message_label.config(text='Invalid username or password. Please sign up.')
        login_frame.pack_forget()
        signup_frame.pack()

# function to create a new user and return to login page
def signup():
    username = new_username_entry.get()
    password = new_password_entry.get()
    users[username] = password
    signup_frame.pack_forget()
    login_frame.pack()

# create the GUI
root = tk.Tk()
root.title('Sign in')
root.geometry('300x250')

# create the login frame
login_frame = tk.Frame(root)
login_frame.pack()

# create the username label and entry
username_label = tk.Label(login_frame, text='Username:')
username_label.pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

# create the password label and entry
password_label = tk.Label(login_frame, text='Password:')
password_label.pack()
password_entry = tk.Entry(login_frame, show='*')
password_entry.pack()

# create the login button
login_button = tk.Button(login_frame, text='Login', command=login)
login_button.pack()

# create the message label
message_label = tk.Label(login_frame, text='')
message_label.pack()

# create the sign-up frame
signup_frame = tk.Frame(root)

# create the new username label and entry
new_username_label = tk.Label(signup_frame, text='New username:')
new_username_label.pack()
new_username_entry = tk.Entry(signup_frame)
new_username_entry.pack()

# create the new password label and entry
new_password_label = tk.Label(signup_frame, text='New password:')
new_password_label.pack()
new_password_entry = tk.Entry(signup_frame, show='*')
new_password_entry.pack()

# create the sign-up button
signup_button = tk.Button(signup_frame, text='Sign up', command=signup)
signup_button.pack()

# create the back button
back_button = tk.Button(signup_frame, text='Back', command=lambda: signup_frame.pack_forget() or login_frame.pack())
back_button.pack()

# create the login/enter button
enter_button = tk.Button(login_frame, text='Enter', command=login)
enter_button.pack()

# create the sign-up button
signup_nav_button = tk.Button(login_frame, text='Sign up', command=lambda: login_frame.pack_forget() or signup_frame.pack())
signup_nav_button.pack()

# run the GUI
root.mainloop()
