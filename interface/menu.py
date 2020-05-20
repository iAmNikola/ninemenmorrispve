from modules.board import Board
from service.minimax import *
from interface.inputs import *
import time

class Menu:
    def __init__(self):
        self.choices = {
                "1": self.play,
                "2": self.quit_app
                }

    @staticmethod
    def display_menu():
        print("1. Počnite igru\n"
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
        alpha = float("-inf")
        beta = float("inf")
        #init board
        board = Board()
        board = Tree(board)
        print(board.value)
        for i in range(9):
            while True:
                position = position_input("Postavite 'W'")
                if board.value.dict[position].middle is "O":
                    break
                print("Odabrano polje je već zauzeto.")
            board.value.dict[position].middle = "W"
            if is_in_mill(position, "W", board.value):
                print(board.value)
                while True:
                    mill = position_input("Uklonite 'B'")
                    if board.value.dict[mill].middle is "B":
                        if is_in_mill(mill, "B", board.value):
                            print("Odabrana figura je u mici.")
                        board.value.dict[mill].middle = "O"
                        break
                    print("Niste odabrali polje na kojem je 'B'.")

            start = time.time()
            best_move = minimaxAB(board, 3, True, alpha, beta, True)
            end = time.time()
            board = best_move.board
            print(board.value)
            print("Potez obavljen: " + str(end - start))





    @staticmethod
    def quit_app():
        print("Izlazak iz programa.")
        quit()


if __name__ == "__main__":
    Menu().run()
