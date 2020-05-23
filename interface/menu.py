
from service.heuristics import *
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
        # stage 1
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
                            continue
                        board.value.dict[mill].middle = "O"
                        break
                    print("Niste odabrali polje na kojem je 'B'.")

            start = time.time()
            best_move = minimaxAB(board, 3, True, alpha, beta, 1)
            end = time.time()
            board = best_move.board
            print(board.value)
            print("Vreme izvršavanja: " + str(end - start))

        _, _, win, human, ai = diff_pieces_blocked("W", board.value)
        if win is 1:
            print("Pobedili ste!")
            exit()
        if win is -1:
            print("Izgubili ste!")
            exit()
        # stage 2 and 3
        stage3 = False
        human, ai = count_pieces(board, "W")
        while True:
            while True:
                cords = move_position_input()
                if board.value.dict[cords[0]].middle is "W":
                    if human is 3 or adjacent(cords):
                        if board.value.dict[cords[1]].middle is "O":
                            break
                        else:
                            print("Odabrano polje je već zauzeto.")
                    else:
                        print("Unešene koordinate nisu susedne.")
                else:
                    print("Niste odabrali polje na kojem je 'W'.")
            board.value.dict[cords[0]].middle = "O"
            board.value.dict[cords[1]].middle = "W"
            if is_in_mill(cords[1], "W", board.value):
                print(board.value)
                while True:
                    mill = position_input("Uklonite 'B'")
                    if board.value.dict[mill].middle is "B":
                        if is_in_mill(mill, "B", board.value):
                            print("Odabrana figura je u mici.")
                            continue
                        board.value.dict[mill].middle = "O"
                        break
                    print("Niste odabrali polje na kojem je 'B'.")
                _,_,win,human, ai = diff_pieces_blocked("W", board.value)
                if win is 1:
                    print("Pobedili ste!")
                    exit()
                if ai is 3:
                    stage3 = True
                if stage3:
                    if human is ai:
                        print("Nerešeno")
                        exit()
            if stage3:
                start = time.time()
                best_move = minimaxAB(board, 1, True, alpha, beta, 3)
            else:
                start = time.time()
                best_move = minimaxAB(board, 4, True, alpha, beta, 2)
            end = time.time()
            board = best_move.board
            print(board.value)
            print("Vreme izvršavanja: " + str(end - start))
            _, _, win, human, ai = diff_pieces_blocked("W", board.value)
            if win is -1:
                print("Izgubili ste!")
                exit()
            if stage3:
                if human is ai:
                    print("Nerešeno")
                    exit()


    @staticmethod
    def quit_app():
        print("Izlazak iz programa.")
        quit()


if __name__ == "__main__":
    Menu().run()
