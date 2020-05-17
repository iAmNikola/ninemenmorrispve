# ━┃
import os

class Menu:
    def __init__(self):
        self.choices = {
                "1": self.play,
                "2": self.quit_app
                }

    @staticmethod
    def display_menu():
        print("1. Izaberite igrača\n"
              "2. Izlazak iz programa")

    def run(self):
        """Displays menu and executes choice."""
        while True:
            self.display_menu()
            choice = input("Izaberite opciju: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} nije validan izbor.".format(choice))

    @staticmethod
    def play():
        player = choose_player()




    @staticmethod
    def quit_app():
        print("Izlazak iz programa.")
        quit()


def print_choices():
    print("1. W (prvi)\n"
          "2. B (drugi)")


def choose_player():
    choices = {
        "1": "W",
        "2": "B",
    }
    while True:
        print_choices()
        choice = input("Izaberite opciju: ")
        player = choices.get(choice)
        if player:
            return player
        else:
            print("{0} nije validan izbor.".format(choice))


def cls():
    """Clears the terminal screen depending on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    Menu().run()
