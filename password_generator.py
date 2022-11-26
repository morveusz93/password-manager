import json
import random
from tkinter import messagebox

import pyperclip

from settings import SYMBOLS


class PasswordGenerator:
    def __init__(self, gui) -> None:
        self.gui = gui

    def passwordgen(self):
        leng = random.randint(8,15)
        chars = [random.choice(SYMBOLS) for char in range(leng)]
        password = "".join(chars)
        self.gui.entry_pass.delete(0, 'end')
        self.gui.entry_pass.insert(0, password)
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def delete_entries(self):
        self.gui.entry_pass.delete(0, 'end')
        self.gui.entry_website.delete(0, 'end')


    def save_to_file(self):
        website = self.gui.entry_website.get()
        login = self.gui.entry_login.get()
        password = self.gui.entry_pass.get()
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
                self.delete_entries()

    def search_password(self):
        website = self.gui.entry_website.get()
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
