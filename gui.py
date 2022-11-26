from tkinter import Button, Canvas, Entry, Label, PhotoImage, Tk

from settings import BG_COLOR, LABEL_FONT, LOGO_PATH, main_login
from PIL import Image, ImageTk

class Gui:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg=BG_COLOR)
        self.create_logo()
        self.create_labels()
        self.create_entries()

    def create_logo(self):
        image = Image.open(LOGO_PATH)
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo, bg=BG_COLOR)
        label.image = photo
        label.grid(row=0, column=1)

    def create_labels(self):
        label_website = Label(text="Website name:", font=LABEL_FONT, bg=BG_COLOR, highlightthickness=0)
        label_website.grid(row=1, column=0)

        label_login = Label(text="Login/email:", font=LABEL_FONT, bg=BG_COLOR, highlightthickness=0)
        label_login.grid(row=2, column=0)

        label_pass = Label(text="Password:", font=LABEL_FONT, bg=BG_COLOR, highlightthickness=0)
        label_pass.grid(row=3, column=0)

    def create_entries(self):
        self.entry_website = Entry(width=32)
        self.entry_website.focus()
        self.entry_website.grid(row=1, column=1)

        self.entry_login = Entry(width=50)
        self.entry_login.insert(0, main_login)
        self.entry_login.grid(row=2, column=1, columnspan=2)

        self.entry_pass = Entry(width=32)
        self.entry_pass.grid(row=3, column=1)

    def create_buttons(self, search_command, generate_command, save_command):
        find_password_btn = Button(text="Search", bg=BG_COLOR, width=14, highlightthickness=0, command=search_command)
        find_password_btn.grid(row=1, column=2)

        generate_pass_btn = Button(text="Generate password", bg=BG_COLOR, highlightthickness=0, command=generate_command)
        generate_pass_btn.grid(row=3, column=2)

        submit_btn = Button(text="Submit", width=42, bg=BG_COLOR, highlightthickness=0, command=save_command)
        submit_btn.grid(row=4, column=1, columnspan=2)
