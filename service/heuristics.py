from modules.board import Board

def diff_mills_and_two(player, board):
    mill_difference = 0
    two_difference = 0
    human_mill = 0
    ai_mill = 0
    horizontal_mills = ["A4", "B4", "C4", "D2", "D6", "E4", "F4", "G4"]
    vertical_mills = ["B4", "D1", "D2", "D3", "D5", "D6", "D7", "F4"]
    for key in horizontal_mills[:]:
        if board.dict[key].middle is player and (board.dict[key].left.middle is player or board.dict[key].right.middle is player):
            two_difference += 1
            if board.dict[key].left.middle is player and board.dict[key].right.middle is player:
                two_difference += 1
                mill_difference += 1
                human_mill += 1
            horizontal_mills.remove(key)
    for key in vertical_mills[:]:
        if board.dict[key].middle is player and (board.dict[key].up.middle is player or board.dict[key].down.middle is player):
            two_difference += 1
            if board.dict[key].up.middle is player and board.dict[key].down.middle is player:
                two_difference += 1
                mill_difference += 1
                human_mill += 1
            vertical_mills.remove(key)
    for key in horizontal_mills:
        if not (board.dict[key].middle is [player, "O"] and (board.dict[key].left.middle is [player, "O"] or board.dict[key].right.middle is [player, "O"])):
            two_difference -= 1
            if not (board.dict[key].left.middle is [player, "O"] and board.dict[key].right.middle is [player, "O"]):
                two_difference -= 1
                mill_difference -= 1
                ai_mill += 1
    for key in vertical_mills:
        if not (board.dict[key].middle is [player, "O"] and (board.dict[key].up.middle is [player, "O"] and board.dict[key].down.middle is [player, "O"])):
            two_difference -= 1
            if not (board.dict[key].up.middle is [player, "O"] and board.dict[key].down.middle is [player, "O"]):
                two_difference -= 1
                mill_difference -= 1
                ai_mill += 1
    return mill_difference, human_mill, ai_mill, two_difference


def count_player_mill(player, board):
    player_mill = 0
    horizontal_mills = ["A4", "B4", "C4", "D2", "D6", "E4", "F4", "G4"]
    vertical_mills = ["B4", "D1", "D2", "D3", "D5", "D6", "D7", "F4"]

    for key in horizontal_mills:
        if board.dict[key].middle is player and board.dict[key].left.middle is player and board.dict[key].right.middle is player:
            player_mill += 1
    for key in vertical_mills:
        if board.dict[key].middle is player and board.dict[key].up.middle is player and board.dict[key].down.middle is player:
            player_mill += 1

    return player_mill


def diff_pieces_blocked(player, board):
    blocked_difference = 0
    human = 0
    human_blocked = 0
    enemy = 0
    enemy_blocked = 0
    win = 0

    for field in board.dict.values():
        if field.middle not in [player, "O"]:
            enemy += 1
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
            enemy_blocked += 1
            blocked_difference += 1

        elif field.middle is player:
            human += 1
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
            human_blocked += 1
            blocked_difference -= 1
    piece_difference = player - enemy
    if enemy is enemy_blocked:
        win += 1
    elif player is human_blocked:
        win -= 1
    if enemy is 2:
        win += 1
    elif player is 2:
        win -= 1

    return piece_difference, blocked_difference, win


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

def is_in_mill(mill, player, board):
    vertical = 0
    horizontal = 0
    if board.dict[mill].up:
        if board.dict[mill].up.middle not in [player, "O"]:
            vertical += 1
            if board.dict[mill].up.up:
                if board.dict[mill].up.up.middle not in [player, "O"]:
                    return True
    if board.dict[mill].down:
        if board.dict[mill].down.middle not in [player, "O"]:
            vertical += 1
            if board.dict[mill].down.down:
                if board.dict[mill].down.down.middle not in [player, "O"]:
                    return True
    if vertical is 2:
        return True
    if board.dict[mill].left:
        if board.dict[mill].left.middle not in [player, "O"]:
            horizontal += 1
            if board.dict[mill].left.left:
                if board.dict[mill].left.left.middle not in [player, "O"]:
                    return True
    if board.dict[mill].right:
        if board.dict[mill].right.middle not in [player, "O"]:
            horizontal += 1
            if board.dict[mill].right.right:
                if board.dict[mill].right.right.middle not in [player, "O"]:
                    return True
    if horizontal is 2:
        return True
    return False









