from gui import Gui
from password_generator import PasswordGenerator


def main():
    gui = Gui()
    app = PasswordGenerator(gui)
    gui.create_buttons(app.search_password, app.passwordgen, app.save_to_file)

    gui.window.mainloop()

if __name__ == "__main__":
    main()