from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

LABEL_FONT = ("Georgia", 12)
GREY = "#8f8c8c"
main_login = "main_login@email.com"

# ---------------------------- SEARCH PASSWORD ----------------------------#

def search_password():
    website = entry_website.get()
    try:
        with open("datafile.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message="File not Found!\nYou don't have any password saved yet")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Login: {data[website]['Login']}\nPassword: {data[website]['Password']}")
        else:
            messagebox.showinfo(title=website, message=f"You don't have saved password to {website}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passwordgen():
    leng = random.randint(8,15)
    symbols = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM.?!#%^*-_=+:;1234567890'
    chars = [random.choice(symbols) for char in range(leng)]
    password = "".join(chars)
    entry_pass.delete(0, 'end')
    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def delete_entries():
    entry_pass.delete(0, 'end')
    entry_website.delete(0, 'end')


def save_to_file():
    website = entry_website.get()
    login = entry_login.get()
    password = entry_pass.get()
    if len(website) == 0 or len(login) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty fields detected!", message="Please don't leave any field empty!")
    else:
        new_data = {
            website: {
                "Login": login,
                "Password": password
            }
        }
        try:
            with open("datafile.json", "r") as file:
                data_from_file = json.load(file)
        except FileNotFoundError:
            with open("datafile.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data_from_file.update(new_data)
            with open("datafile.json", 'w') as file:
                json.dump(data_from_file, file, indent=4)
        finally:
            messagebox.showinfo(title=website, message="Saved!")
            delete_entries()

# ---------------------------- UI SETUP ------------------------------- #
# WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=GREY)
# CANVAS
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.config(bg=GREY, highlightthickness=0)
canvas.grid(row=0, column=1)

# LABELS
label_website = Label(text="Website name:", font=LABEL_FONT, bg=GREY, highlightthickness=0)
label_website.grid(row=1, column=0)

label_login = Label(text="Login/email:", font=LABEL_FONT, bg=GREY, highlightthickness=0)
label_login.grid(row=2, column=0)

label_pass = Label(text="Password:", font=LABEL_FONT, bg=GREY, highlightthickness=0)
label_pass.grid(row=3, column=0)

# ENTRIES
entry_website = Entry(width=32)
entry_website.focus()
entry_website.grid(row=1, column=1)

entry_login = Entry(width=50)
entry_login.insert(0, main_login)
entry_login.grid(row=2, column=1, columnspan=2)

entry_pass = Entry(width=32)
entry_pass.grid(row=3, column=1)

# BUTTONS
find_password_btn = Button(text="Search", bg=GREY, width=14, highlightthickness=0, command=search_password)
find_password_btn.grid(row=1, column=2)

generate_pass_btn = Button(text="Generate password", bg=GREY, highlightthickness=0, command=passwordgen)
generate_pass_btn.grid(row=3, column=2)

submit_btn = Button(text="Submit", width=42, bg=GREY, highlightthickness=0, command=save_to_file)
submit_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()