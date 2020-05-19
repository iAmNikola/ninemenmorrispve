from service.heuristics import *
from interface.inputs import *

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
        human_mills = 0
        ai_mills = 0

        #init board
        board = Board()
        player = choose_player()
        if player is "W":
            for i in range(9):
                print(board)
                while True:
                    position = position_input("INIT")
                    if board.dict[position].middle is "O":
                        break
                    print("Odabrano polje je već zauzeto.")
                board.dict[position].middle = player
                new_human_mills = count_player_mill(player, board)
                if new_human_mills > human_mills:
                    while True:
                        mill = position_input("MILL")
                        if board.dict[mill].middle not in [player, "O"]:
                            if is_in_mill(mill, player, board):
                                print("Odabrana figura je u mici.")
                            board.dict[mill].middle = "O"




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




if __name__ == "__main__":
    Menu().run()
