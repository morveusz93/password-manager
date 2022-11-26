
# TODO: 
# 2. Hashowanie haseł
# 3. Info na przycisku o skopiowaniu hasła
# 4. Settingsy do generowania hasła 
#   a. liczba znaków
#   b. duże i małe litery?
#   c. liczba znaków specjalnych
#   d. liczba cyfr i liter
# 5. REDAME z screen shotami

from gui import Gui
from password_generator import PasswordGenerator


def main():
    gui = Gui()
    app = PasswordGenerator(gui)
    gui.create_buttons(app.search_password, app.passwordgen, app.save_to_file)

    gui.window.mainloop()

if __name__ == "__main__":
    main()