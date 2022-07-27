from tkinter import *
import os
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

EMAIL = ""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_key():
    pass_letters = [choice(letters) for char in range(randint(8, 10))]
    pass_numbers = [choice(numbers) for char in range(randint(2, 4))]
    pass_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_list = pass_letters + pass_numbers + pass_symbols
    shuffle(password_list)

    gen_password = ''.join(password_list)
    pass_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
here = os.path.dirname(os.path.abspath(__file__))
save_file = os.path.join(here, 'data.json')


def get_data():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='hmm', message='seems you forgot somethin bud')
    else:
        try:
            with open(save_file, 'r') as completed:
                data = json.load(completed)

        except FileNotFoundError:
            with open(save_file, 'w') as completed:
                json.dump(new_data, completed, indent=4)
        else:
            data.update(new_data)
            with open(save_file, 'w') as completed:
                json.dump(data, completed, indent=4)
        finally:
            pass_entry.delete(0, END)
            web_entry.delete(0, END)

#-----------------------------SEARCH FOR PASSWORD --------------------#


def search_action():
    try:
        req_web = web_entry.get().title()
        with open(save_file, 'r') as requested:
            req_data = json.load(requested)
        req_email = (req_data[req_web]['email'])
        req_pass = req_data[req_web]['password']
        web_entry.delete(0, END)
        web_entry.insert(0, str(req_web))
        email_entry.delete(0, END)
        email_entry.insert(0, str(req_email))
        pass_entry.delete(0, END)
        pass_entry.insert(0, str(req_pass))
    except:
        pass


# ---------------------------- UI SETUP ------------------------------- #
# Setup Window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Import logo img as canvas background
canvas = Canvas(width=200, height=200, highlightthickness=0)
file = os.path.join(here, 'logo.png')
logo_img = PhotoImage(file=file)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Create labels
website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username: ')
email_label.grid(column=0, row=2)

pass_label = Label(text='Password: ')
pass_label.grid(column=0, row=3)

# Create Entries
web_entry = Entry(width=37)
web_entry.grid(column=1, row=1, columnspan=1)
web_entry.focus()

email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, EMAIL)

pass_entry = Entry(width=37)
pass_entry.grid(column=1, row=3)

# Create buttons
gen_button = Button(text='Generate Password', width=14, command=generate_key)
gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=46, command=get_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=14, command=search_action)
search_button.grid(column=2, row=1)

window.mainloop()
