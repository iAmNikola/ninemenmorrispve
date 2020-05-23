from .logic import *
from modules.best_move import BestMove
from service.heuristics import *

def minimaxAB(board, depth, bot, alpha, beta, stage):
    player = "W"
    ai = "B"
    best_move = BestMove()

    if depth is not 0:
        if bot:
            if stage is 1:
                stage1_moves(board, ai)
            elif stage is 2:
                stage2_moves(board, ai)
            else:
                stage3_moves(board, ai)
        else:
            if stage is 1:
                stage1_moves(board, player)
            elif stage is 2:
                stage2_moves(board, player)
            else:
                stage3_moves(board, player)
        for move in board.children:
            playa, opponent = count_pieces(move, "W")
            if bot:
                if stage is 3:
                    if opponent > 3:
                        current_move = minimaxAB(move, depth-1, False, alpha, beta, 2)
                    else:
                        current_move = minimaxAB(move, depth - 1, False, alpha, beta, stage)
                else:
                    current_move = minimaxAB(move, depth-1, False, alpha, beta, stage)
                if current_move.value > alpha:
                    alpha = current_move.value
                    best_move.board = move
            else:
                if stage is 3:
                    if playa > 3:
                        current_move = minimaxAB(move, depth-1, True, alpha, beta, 2)
                    else:
                        current_move = minimaxAB(move, depth - 1, True, alpha, beta, stage)
                else:
                    current_move = minimaxAB(move, depth-1, True, alpha, beta, stage)
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
            best_move.value = heuristic(board, ai, stage)
        else:
            best_move.value = -(heuristic(board, player, stage))

    return best_move
