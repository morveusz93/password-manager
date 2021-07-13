from tkinter import *

LABEL_FONT = ("Georgia", 12)
GREY = "#8f8c8c"
main_login = "main_login@email.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def delete_entries():
    entry_pass.delete(0, 'end')
    entry_website.delete(0, 'end')

def save_to_file():
    website = entry_website.get()
    login = entry_login.get()
    password = entry_pass.get()
    data = f"{website} | {login} | {password}\n"
    with open("datafile.txt", "a") as file:
        file.write(data)
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
entry_website = Entry(width=50)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

entry_login = Entry(width=50)
entry_login.insert(0, main_login)
entry_login.grid(row=2, column=1, columnspan=2)

entry_pass = Entry(width=32)
entry_pass.grid(row=3, column=1)

# BUTTONS
generate_pass_btn = Button(text="Generate password", bg=GREY, highlightthickness=0)
generate_pass_btn.grid(row=3, column=2)

submit_btn = Button(text="Submit", width=42, bg=GREY, highlightthickness=0, command=save_to_file)
submit_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()