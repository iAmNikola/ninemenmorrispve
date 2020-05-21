from modules.tree import Tree
from copy import deepcopy


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
                boards = remove_piece(board_clone, boards, opponent)
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
                        boards = remove_piece(board_clone, boards, opponent)
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
                            boards = remove_piece(board_clone, boards, opponent)
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
                            boards = remove_piece(board_clone, boards, opponent)
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


def remove_piece(board, boards, opponent):
    for field in board.value.dict.keys():
        if board.value.dict[field].middle is opponent:
            if not is_in_mill(field, opponent, board.value):
                new_board = deepcopy(board.value)
                new_board.dict[field].middle = "O"
                boards.append(Tree(new_board, board))
    return boards

