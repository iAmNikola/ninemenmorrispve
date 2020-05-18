import os


def cls():
    """Clears the terminal screen depending on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


def move_input():
    while True:
        move = input("Potez: ")
        if move.capitalize() not in ["MOVE", "INIT", "MILL"]:
            print("Uneli ste nepostojeći potez.\n Postojeći potezi su: INIT, MOVE, MILL.")
            continue
        return move.capitalize()


def position_input(move):
    fields = ["A1", "A4", "A7", "B2", "B4", "B6", "C3", "C4", "C5", "D1", "D2", "D3",
              "D5", "D6", "D7", "E3", "E4", "E5", "F2", "F4", "F6", "G1", "G4", "G7"]
    while True:
        position = input("Koordinati za"+move+": ")
        if position not in fields:
            print("{} nije važeći potez, npr. E5.".format(position))
            continue
        return position


def move_position_input():
    fields = ["A1", "A4", "A7", "B2", "B4", "B6", "C3", "C4", "C5", "D1", "D2", "D3",
              "D5", "D6", "D7", "E3", "E4", "E5", "F2", "F4", "F6", "G1", "G4", "G7"]
    while True:
        position = input("Koordinati za MOVE: ")
        cords = position.replace(" ", "").split(",")
        if len(cords) != 2 and cords[0] not in fields and cords[1] not in fields:
            print("Niste uneli važeće koordinate. Npr. F2, F4.")
            continue
        return cords
