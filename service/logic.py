from service.heuristics import heuristic
from modules.tree import Tree
from copy import deepcopy


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



def stage23_moves(board, player):
    pass


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

