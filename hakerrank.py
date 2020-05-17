# def next-move(state, depth):
#
#
# bestMove = nil
# alpha = -INF
# for next - state in state.nexts():
#     result = minscore(next - state, depth - 1, alpha, INF)
#     if result > alpha:
#         alpha = result
#         bestMove = next - state.move()
#     if alpha >= MAX - POSSIBLE - SCORE:
#         break
# return bestMove
#
#
# def maxscore(state, depth, alpha, beta):
#     if isTerminal(state):
#         return goal - value(state)
#     if depth <= 0:
#         return heuristic - value(state)
#     for next - state in state.nexts():
#         score = minscore(next, depth - 1, alpha, beta)
#         alpha = max(alpha, score)
#         if alpha >= beta:
#             return beta
#     return alpha
#
#
# def minscore(state, depth, alpha, beta):
#     if isTerminal(state):
#         return goal - value(state)
#     if depth <= 0:
#         return heuristic - value(state)
#     for next - state in state.nexts():
#         score = maxscore(next, depth - 1, alpha, beta)
#         beta = min(beta, score)
#         if alpha >= beta:
#             return alpha
#     return beta