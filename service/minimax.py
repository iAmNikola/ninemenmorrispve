from .logic import *
from modules.best_move import BestMove


def minimaxAB(board, depth, bot, alpha, beta, is_stage1):
    player = "W"
    ai = "B"
    best_move = BestMove()

    if depth is not 0:
        if bot:
            if is_stage1:
                stage1_moves(board, ai)
            else:
                stage23_moves(board, ai)
        else:
            if is_stage1:
                stage1_moves(board, player)
            else:
                stage23_moves(board, player)
        for move in board.children:
            if bot:
                current_move = minimaxAB(move, depth-1, False, alpha, beta, is_stage1)
                if current_move.value > alpha:
                    alpha = current_move.value
                    best_move.board = move
            else:
                current_move = minimaxAB(move, depth-1, True, alpha, beta, is_stage1)
                if current_move.value < beta:
                    beta = current_move.value
                    best_move.board = move
            if alpha >= beta:
                break
        if bot:
            best_move.value = alpha
        else:
            best_move.value = beta
    else:
        if bot:
            best_move.value = heuristic(board, ai, is_stage1)
        else:
            best_move.value = -(heuristic(board, player, is_stage1))

    return best_move
