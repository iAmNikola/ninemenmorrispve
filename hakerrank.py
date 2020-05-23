from copy import deepcopy
import time

# CLASSES
# -------------------------------------------------------------------------
class BestMove:
    def __init__(self):
        self.value = 0
        self.board = None


class Tree:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []


class Field:
    def __init__(self, value):
        self.middle = value
        self.up = None
        self.down = None
        self.left = None
        self.right = None


class Board:
    def __init__(self, f1, f2, f3, f9, f10, f11, f17, f18, f19, f8, f16, f24, f20, f12, f4, f23, f22, f21, f15, f14, f13, f7, f6, f5):
        """Connects all of the fields."""
        self.f1 = Field(f1);self.f2 = Field(f2);self.f3 = Field(f3); self.f4 = Field(f4)
        self.f5 = Field(f5);self.f6 = Field(f6);self.f7 = Field(f7);self.f8 = Field(f8)
        self.f9 = Field(f9);self.f10 = Field(f10);self.f11 = Field(f11);self.f12 = Field(f12)
        self.f13 = Field(f13);self.f14 = Field(f14);self.f15 = Field(f15);self.f16 = Field(f16)
        self.f17 = Field(f17);self.f18 = Field(f18);self.f19 = Field(f19);self.f20 = Field(f20)
        self.f21 = Field(f21);self.f22 = Field(f22);self.f23 = Field(f23);self.f24 = Field(f24)

        self.f1.down = self.f8; self.f1.right = self.f2
        self.f2.down = self.f10; self.f2.left = self.f1; self.f2.right = self.f3
        self.f3.down = self.f4; self.f3.left = self.f2
        self.f4.up = self.f3; self.f4.down = self.f5; self.f4.left = self.f12
        self.f5.up = self.f4; self.f5.left = self.f6
        self.f6.up = self.f14; self.f6.left = self.f7; self.f6.right = self.f5
        self.f7.up = self.f8; self.f7.right = self.f6
        self.f8.up = self.f1; self.f8.down = self.f7; self.f8.right = self.f16
        self.f9.down = self.f16; self.f9.right = self.f10
        self.f10.up = self.f2; self.f10.down = self.f18; self.f10.left = self.f9; self.f10.right = self.f11
        self.f11.down = self.f12; self.f11.left = self.f10
        self.f12.up = self.f11; self.f12.down = self.f13; self.f12.left = self.f20; self.f12.right = self.f4
        self.f13.up = self.f12; self.f13.left = self.f14
        self.f14.up = self.f22; self.f14.down = self.f6; self.f14.left = self.f15; self.f14.right = self.f13
        self.f15.up = self.f16; self.f15.right = self.f14
        self.f16.up = self.f9; self.f16.down = self.f15; self.f16.left = self.f8; self.f16.right = self.f24
        self.f17.down = self.f24; self.f17.right = self.f18
        self.f18.up = self.f10; self.f18.left = self.f17; self.f18.right = self.f19
        self.f19.down = self.f20; self.f19.left = self.f18
        self.f20.up = self.f19; self.f20.down = self.f21; self.f20.right = self.f12
        self.f21.up = self.f20; self.f21.left = self.f22
        self.f22.down = self.f14; self.f22.left = self.f23; self.f22.right = self.f21
        self.f23.up = self.f24; self.f23.right = self.f22
        self.f24.up = self.f17; self.f24.down = self.f23; self.f24.left = self.f16

        self.dict = {"A1": self.f1, "A4": self.f2, "A7": self.f3,
                     "B2": self.f9, "B4": self.f10, "B6": self.f11,
                     "C3": self.f17, "C4": self.f18, "C5": self.f19,
                     "D1": self.f8, "D2": self.f16, "D3": self.f24, "D5": self.f20, "D6": self.f12, "D7": self.f4,
                     "E3": self.f23, "E4": self.f22, "E5": self.f21,
                     "F2": self.f15, "F4": self.f14, "F6": self.f13,
                     "G1": self.f7, "G4": self.f6, "G7": self.f5}


# MINIMAX
# -------------------------------------------------------------------------
def minimaxAB(board, depth, my_turn, alpha, beta, stage, you):
    players = ["W", "B"]
    players.remove(you)
    ai = players[0]
    best_move = BestMove()

    if depth is not 0:
        if my_turn:
            if stage is 1:
                stage1_moves(board, you)
            elif stage is 2:
                stage2_moves(board, you)
            elif stage is 3:
                stage3_moves(board, you)
            else:
                remove_piece_minimax(board, ai)
        else:
            if stage is 1:
                stage1_moves(board, ai)
            elif stage is 2:
                stage2_moves(board, ai)
            elif stage is 3:
                stage3_moves(board, ai)
            else:
                remove_piece_minimax(board, you)
        for move in board.children:
            playa, _ = count_pieces(move, you)
            if my_turn:
                if stage is 4:
                    current_move = minimaxAB(move, depth-1, False, alpha, beta, 1, ai)
                elif stage is 3:
                    if playa > 3:
                        current_move = minimaxAB(move, depth-1, False, alpha, beta, 2, ai)
                    else:
                        current_move = minimaxAB(move, depth - 1, False, alpha, beta, stage, ai)
                else:
                    current_move = minimaxAB(move, depth-1, False, alpha, beta, stage, ai)
                if current_move.value > alpha:
                    alpha = current_move.value
                    best_move.board = move
            else:
                if stage is 4:
                    current_move = minimaxAB(move, depth-1, True, alpha, beta, 1, you)
                elif stage is 3:
                    if playa > 3:
                        current_move = minimaxAB(move, depth - 1, True, alpha, beta, 2, you)
                    else:
                        current_move = minimaxAB(move, depth - 1, True, alpha, beta, stage, you)
                else:
                    current_move = minimaxAB(move, depth-1, True, alpha, beta, stage, you)
                if current_move.value < beta:
                    beta = current_move.value
                    best_move.board = move
            if alpha >= beta:
                break
        if my_turn:
            best_move.value = alpha
        else:
            best_move.value = beta
    else:
        if my_turn:
            best_move.value = heuristic(board, you, stage)
        else:
            best_move.value = -(heuristic(board, ai, stage))

    return best_move


# LOGIC
# -------------------------------------------------------------------------

def remove_piece_minimax(board, opponent):
    boards = []

    for field in board.value.dict.keys():
        if board.value.dict[field].middle is opponent:
            if not is_in_mill(field, opponent, board.value):
                new_board = deepcopy(board.value)
                new_board.dict[field].middle = "O"
                boards.append(Tree(new_board, board))
    for b in boards:
        b.parent = board
    board.children = boards




def adjacent(cords, return_list=False):
    adjacent_fileds = {"A1": ["A4", "D1"],
                       "A4": ["A1", "A7", "B4"],
                       "A7": ["A4", "D7"],
                       "B2": ["B4", "D2"],
                       "B4": ["A4", "B2", "B6", "C4"],
                       "B6": ["B4", "D6"],
                       "C3": ["C4", "D3"],
                       "C4": ["B4", "C3", "C5"],
                       "C5": ["C4", "D5"],
                       "D1": ["A1", "D2", "G1"],
                       "D2": ["B2", "D1", "D3", "F2"],
                       "D3": ["C3", "D2", "E3"],
                       "D5": ["C5", "D6", "E5"],
                       "D6": ["B6", "D5", "D7", "F6"],
                       "D7": ["A7", "D6", "G7"],
                       "E3": ["D3", "E4"],
                       "E4": ["E3", "E5", "F4"],
                       "E5": ["D5", "E4"],
                       "F2": ["D2", "F4"],
                       "F4": ["E4", "F2", "F6", "G4"],
                       "F6": ["D6", "F4"],
                       "G1": ["D1", "G4"],
                       "G4": ["F4", "G1", "G7"],
                       "G7": ["D7", "G4"]
                       }
    if return_list:
        return adjacent_fileds[cords]
    if cords[1] in adjacent_fileds[cords[0]]:
        return True
    return False


def stage1_moves(board, player):
    players = ["W", "B"]
    players.remove(player)
    opponent = players[0]
    boards = []

    for field in board.value.dict.keys():
        if board.value.dict[field].middle is "O":
            board_clone = deepcopy(board.value)
            board_clone = Tree(board_clone, board)
            board_clone.value.dict[field].middle = player
            if is_in_mill(field, player, board_clone.value):
                remove_piece(board_clone, opponent)
            else:
                boards.append(board_clone)
    for b in boards:
        b.parent = board
    board.children = boards


def stage2_moves(board, player):
    players = ["W", "B"]
    players.remove(player)
    opponent = players[0]
    boards = []

    for field in board.value.dict.keys():
        if board.value.dict[field].middle is player:
            adjacent_list = adjacent(field, True)
            for cord in adjacent_list:
                if board.value.dict[cord].middle is "O":
                    board_clone = deepcopy(board.value)
                    board_clone = Tree(board_clone, board)
                    board_clone.value.dict[field].middle = "O"
                    board_clone.value.dict[cord].middle = player
                    if is_in_mill(cord, player, board_clone.value):
                        remove_piece(board_clone, opponent)
                    else:
                        boards.append(board_clone)
    for b in boards:
        b.parent = board
    board.children = boards


def stage3_moves(board, player):
    players = ["W", "B"]
    players.remove(player)
    opponent = players[0]
    boards = []

    playa = 0
    for field in board.value.dict.keys():
        if board.value.dict[field].middle is player:
            playa += 1
    for field in board.value.dict.keys():
        if board.value.dict[field].middle is player:
            if playa == 3:
                for pos in board.value.dict.keys():
                    if board.value.dict[pos].middle is "O":
                        board_clone = deepcopy(board.value)
                        board_clone = Tree(board_clone, board)
                        board_clone.value.dict[field].middle = "O"
                        board_clone.value.dict[pos].middle = player
                        if is_in_mill(pos, player, board_clone.value):
                            remove_piece(board_clone, opponent)
                        else:
                            boards.append(board_clone)
            else:
                adjacent_list = adjacent(field, True)
                for cord in adjacent_list:
                    if board.value.dict[cord].middle is "O":
                        board_clone = deepcopy(board.value)
                        board_clone = Tree(board_clone, board)
                        board_clone.value.dict[field].middle = "O"
                        board_clone.value.dict[cord].middle = player
                        if is_in_mill(cord, player, board_clone.value):
                            remove_piece(board_clone, opponent)
                        else:
                            boards.append(board_clone)
    for b in boards:
        b.parent = board
    board.children = boards


def is_in_mill(mill, player, board):
    vertical = 0
    horizontal = 0
    if board.dict[mill].up:
        if board.dict[mill].up.middle is player:
            vertical += 1
            if board.dict[mill].up.up:
                if board.dict[mill].up.up.middle is player:
                    return True
    if board.dict[mill].down:
        if board.dict[mill].down.middle is player:
            vertical += 1
            if board.dict[mill].down.down:
                if board.dict[mill].down.down.middle is player:
                    return True
    if vertical is 2:
        return True
    if board.dict[mill].left:
        if board.dict[mill].left.middle is player:
            horizontal += 1
            if board.dict[mill].left.left:
                if board.dict[mill].left.left.middle is player:
                    return True
    if board.dict[mill].right:
        if board.dict[mill].right.middle is player:
            horizontal += 1
            if board.dict[mill].right.right:
                if board.dict[mill].right.right.middle is player:
                    return True
    if horizontal is 2:
        return True
    return False


def remove_piece(board, opponent):
    boards = []
    for field in board.value.dict.keys():
        if board.value.dict[field].middle is opponent:
            if not is_in_mill(field, opponent, board.value):
                new_board = deepcopy(board.value)
                new_board.dict[field].middle = "O"
                boards.append(Tree(new_board, board))
    board.children = [boards]


# HEURISTIC
# -------------------------------------------------------------------------


def diff_mills_and_two(player, board):
    mill_difference = 0
    two_difference = 0
    blocked_mill_difference = 0
    horizontal_mills = ["A4", "B4", "C4", "D2", "D6", "E4", "F4", "G4"]
    vertical_mills = ["B4", "D1", "D2", "D3", "D5", "D6", "D7", "F4"]
    for key in horizontal_mills[:]:
        if board.dict[key].middle is player and (board.dict[key].left.middle is player or board.dict[key].right.middle is player):
            two_difference += 1
            if board.dict[key].left.middle not in [player, "O"] or board.dict[key].right.middle not in [player, "O"]:
                blocked_mill_difference -= 1
            elif board.dict[key].left.middle is player and board.dict[key].right.middle is player:
                two_difference += 1
                mill_difference += 1
            horizontal_mills.remove(key)
    for key in vertical_mills[:]:
        if board.dict[key].middle is player and (board.dict[key].up.middle is player or board.dict[key].down.middle is player):
            two_difference += 1
            if board.dict[key].up.middle not in [player, "O"] or board.dict[key].down.middle not in [player, "O"]:
                blocked_mill_difference -= 1
            elif board.dict[key].up.middle is player and board.dict[key].down.middle is player:
                two_difference += 1
                mill_difference += 1
            vertical_mills.remove(key)
    for key in horizontal_mills:
        if not (board.dict[key].middle in [player, "O"] and (board.dict[key].left.middle in [player, "O"] or board.dict[key].right.middle in [player, "O"])):
            two_difference -= 1
            if board.dict[key].left.middle is player or board.dict[key].right.middle is player:
                blocked_mill_difference += 1
            elif not (board.dict[key].left.middle in [player, "O"] and board.dict[key].right.middle is [player, "O"]):
                two_difference -= 1
                mill_difference -= 1
    for key in vertical_mills:
        if not (board.dict[key].middle in [player, "O"] and (board.dict[key].up.middle in [player, "O"] and board.dict[key].down.middle in [player, "O"])):
            two_difference -= 1
            if board.dict[key].up.middle is player or board.dict[key].down.middle is player:
                blocked_mill_difference += 1
            elif not (board.dict[key].up.middle in [player, "O"] and board.dict[key].down.middle in [player, "O"]):
                two_difference -= 1
                mill_difference -= 1
    return mill_difference, two_difference, blocked_mill_difference


def diff_pieces_blocked(player, board):
    blocked_difference = 0
    playa = 0
    playa_blocked = 0
    opponent = 0
    opponent_blocked = 0
    win = 0

    for field in board.dict.values():
        if field.middle not in [player, "O"]:
            opponent += 1
            if field.up:
                if field.up.middle is "O":
                    continue
            if field.down:
                if field.down.middle is "O":
                    continue
            if field.left:
                if field.left.middle is "O":
                    continue
            if field.right:
                if field.right.middle is "O":
                    continue
            opponent_blocked += 1
            blocked_difference += 1

        elif field.middle is player:
            playa += 1
            if field.up:
                if field.up.middle is "O":
                    continue
            if field.down:
                if field.down.middle is "O":
                    continue
            if field.left:
                if field.left.middle is "O":
                    continue
            if field.right:
                if field.right.middle is "O":
                    continue
            playa_blocked += 1
            blocked_difference -= 1
    piece_difference = playa - opponent
    if opponent is opponent_blocked:
        win += 1
    elif playa is playa_blocked:
        win -= 1
    if opponent is 2:
        win += 1
    elif playa is 2:
        win -= 1

    return piece_difference, blocked_difference, win, playa, opponent


def diff_double_three(player, board):
    up_left_corner = ["A1", "B2", "C3"]
    up_right_corner = ["A7", "B6", "C5"]
    down_left_corner = ["G1", "F2", "E3"]
    down_right_corner = ["G7", "F6", "E5"]
    cross = ["B4", "D2", "D6", "F4"]
    three_difference = 0
    double_difference = 0

    for field in up_left_corner:
        if board.dict[field].middle is player:
            if board.dict[field].down.middle is player and board.dict[field].right is player:
                three_difference += 1
                if board.dict[field].down.down.middle is player and board.dict[field].right.right.middle is player:
                    double_difference += 1
        elif board.dict[field].middle not in [player, "O"]:
            if board.dict[field].down.middle not in [player, "O"] and board.dict[field].right not in [player, "O"]:
                three_difference -= 1
                if board.dict[field].down.down.middle not in [player, "O"] and board.dict[field].right.right.middle not in [player, "O"]:
                    double_difference -= 1
    for field in up_right_corner:
        if board.dict[field].middle is player:
            if board.dict[field].down.middle is player and board.dict[field].left is player:
                three_difference += 1
                if board.dict[field].down.down.middle is player and board.dict[field].left.left.middle is player:
                    double_difference += 1
        elif board.dict[field].middle not in [player, "O"]:
            if board.dict[field].down.middle not in [player, "O"] and board.dict[field].left not in [player, "O"]:
                three_difference -= 1
                if board.dict[field].down.down.middle not in [player, "O"] and board.dict[field].left.left.middle not in [player, "O"]:
                    double_difference -= 1
    for field in down_left_corner:
        if board.dict[field].middle is player:
            if board.dict[field].up.middle is player and board.dict[field].right is player:
                three_difference += 1
                if board.dict[field].up.up.middle is player and board.dict[field].right.right.middle is player:
                    double_difference += 1
        elif board.dict[field].middle not in [player, "O"]:
            if board.dict[field].up.middle not in [player, "O"] and board.dict[field].right not in [player, "O"]:
                three_difference -= 1
                if board.dict[field].up.up.middle not in [player, "O"] and board.dict[field].right.right.middle not in [player, "O"]:
                    double_difference -= 1
    for field in down_right_corner:
        if board.dict[field].middle is player:
            if board.dict[field].up.middle is player and board.dict[field].left is player:
                three_difference += 1
                if board.dict[field].up.up.middle is player and board.dict[field].left.left.middle is player:
                    double_difference += 1
        elif board.dict[field].middle not in [player, "O"]:
            if board.dict[field].up.middle not in [player, "O"] and board.dict[field].left not in [player, "O"]:
                three_difference -= 1
                if board.dict[field].up.up.middle not in [player, "O"] and board.dict[field].left.left.middle not in [player, "O"]:
                    double_difference -= 1
    for field in cross:
        check = False
        if board.dict[field].middle is player:
            if board.dict[field].up is player and board.dict[field].left is player:
                three_difference += 1
                check = True
            if board.dict[field].up is player and board.dict[field].right is player:
                three_difference += 1
            if board.dict[field].down is player and board.dict[field].left is player:
                three_difference += 1
            if board.dict[field].down is player and board.dict[field].right is player:
                three_difference += 1
                if check:
                    double_difference += 1
        elif board.dict[field].middle not in [player, "O"]:
            if not (board.dict[field].up in [player, "O"] and board.dict[field].left in [player, "O"]):
                three_difference -= 1
                check = True
            if not (board.dict[field].up in [player, "O"] and board.dict[field].right in [player, "O"]):
                three_difference -= 1
            if not (board.dict[field].down in [player, "O"] and board.dict[field].left in [player, "O"]):
                three_difference -= 1
            if not (board.dict[field].down in [player, "O"] and board.dict[field].right in [player, "O"]):
                three_difference -= 1
                if check:
                    double_difference -= 1

    return double_difference, three_difference


def count_pieces(board, player):
    playa = 0
    opponent = 0

    for field in board.value.dict.keys():
        if board.value.dict[field].middle is player:
            playa += 1
        elif board.value.dict[field].middle not in [player, "O"]:
            opponent += 1
    return playa, opponent


def closed_mill(board, player):
    old_playa, old_opponent = count_pieces(board.parent, player)
    playa, opponent = count_pieces(board, player)

    if old_playa is (playa+1):
        return -1
    elif old_opponent is (opponent+1):
        return 1
    else:
        return 0


def heuristic(board, player, stage):
    closed = closed_mill(board, player)
    if stage is 1 or stage is 4:
        mill_diff, two_diff, blocked_mill_diff = diff_mills_and_two(player, board.value)
        piece_diff, blocked_diff, _, _, _ = diff_pieces_blocked(player, board.value)
        _, three_diff = diff_double_three(player, board.value)
        return 18*closed + 26*mill_diff + blocked_diff + 9*piece_diff + 10*two_diff + 7*three_diff + 20*blocked_mill_diff
    elif stage is 2:
        mill_diff, _, blocked_mill_diff = diff_mills_and_two(player, board.value)
        piece_diff, blocked_diff, win, _, _ = diff_pieces_blocked(player, board.value)
        double_diff, _ = diff_double_three(player, board.value)
        return 14*closed + 43*mill_diff + 10*blocked_diff + 8*piece_diff + 42*double_diff + 1086*win + 25*blocked_mill_diff
    else:
        playa, opponent = count_pieces(board, player)
        _, two_diff, blocked_mill_diff = diff_mills_and_two(player, board.value)
        _, three_diff = diff_double_three(player, board.value)
        if playa is 2:
            win = -1
        elif opponent is 2:
            win = 1
        else:
            win = 0
        return 16*closed + 10*two_diff + three_diff + 1190*win + 30*blocked_mill_diff


# HAKERRANK
# -------------------------------------------------------------------------
def nextMove(old, new, player, move):
    position_conversion = {"A1": "0 0", "A4": "0 3","A7": "0 6",
                           "B2": "1 1","B4": "1 3","B6": "1 5",
                           "C3": "2 2","C4": "2 3","C5": "2 4",
                           "D1": "3 0","D2": "3 1","D3": "3 2","D5": "3 4", "D6": "3 5","D7": "3 6",
                           "E3": "4 2","E4": "4 3","E5": "4 4",
                           "F2": "5 1","F4": "5 3","F6": "5 5",
                           "G1": "6 0","G4": "6 3","G7": "6 6",}

    players = ["W", "B"]
    players.remove(player)
    opponent = players[0]

    if move in ["INIT", "MILL"]:
        for p in old.keys():
            if old[p].middle is not new[p].middle:
                return position_conversion[p]
    else:
        for p1 in old.keys():
            if old[p1].middle is player and new[p1].middle == "O":
                for p2 in old.keys():
                    if old[p2].middle == "O" and new[p2].middle is player:
                        return position_conversion[p1]+" "+position_conversion[p2]


if __name__ == '__main__':
    b = []
    best_move = BestMove()
    # input
    player = input()
    move = input()
    for i in range(7):
        row = input()
        b.append(row)

    board = Board(b[0][0], b[0][3], b[0][6],
                  b[1][1], b[1][3], b[1][5],
                  b[2][2], b[2][3], b[2][4],
                  b[3][0], b[3][1], b[3][2], b[3][4], b[3][5], b[3][6],
                  b[4][2], b[4][3], b[4][4],
                  b[5][1], b[5][3], b[5][5],
                  b[6][0], b[6][3], b[6][6])
    board = Tree(board)
    if move == "INIT":
        best_move = minimaxAB(board, 3, True, float("-inf"), float("inf"), 1, player)
    if move == "MOVE":
        you, opp = count_pieces(board, player)
        if you is 3:
            best_move = minimaxAB(board, 1, True, float("-inf"), float("inf"), 3, player)
        else:
            best_move = minimaxAB(board, 4, True, float("-inf"), float("inf"), 2, player)
    if move == "MILL":
        best_move = minimaxAB(board, 3, True, float("-inf"), float("inf"), 4, player)

    old = board.value.dict
    new = best_move.board.value.dict

    print(nextMove(old, new, player, move))
