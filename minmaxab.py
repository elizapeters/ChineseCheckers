from valid_moves import *
from game_initialization import *
from game_over import *
from move import *
import math
from minimax import *

def findAndReplaceMarb(locations, optMove, player):
    for i in range(len(locations[player-1])):
        marb = locations[player-1][i]
        if marb[0] == optMove[0][0] and marb[1] == optMove[0][1]:
            locations[player-1][i] = optMove[1]

def evaluate(board, player):
    # Example: Count how many pieces player has on the board
    count = 0
    return count

# Minimax with Alpha-Beta pruning
def minimax(board, depth, maximizing_player, alpha, beta, player, locations):
    if depth == 0 or game_over(board):
        return -1 * calculate_distance(board, player), (0,0,0,0)

    if maximizing_player:
        max_eval = float('-inf')
        max_move = ((0, 0), (0, 0))
        for i in range(len(locations[player-1])):
            marb = locations[player-1][i]
            all_moves = valid_moves(board, marb, player)
            for x, y in all_moves: 
                boardc = board.copy()
                move(boardc, marb[0], marb[1], x, y)
                locationsc = locations.copy()
                findAndReplaceMarb(locationsc, (marb, (x, y)), player)
                evalu, next_move = minimax(boardc, depth - 1, False, alpha, beta, player, locationsc)
                if evalu > max_eval :
                    max_move = (marb, (x, y))
                    max_eval = max(max_eval, evalu)
                    alpha = max(alpha, evalu)
                    if beta <= alpha:
                        break
        return max_eval, max_move
    else:
        min_eval = float('inf')
        min_move = (0, 0, 0, 0)
        for i in range(len(locations)):
            for j in range(len(locations[i])):
                marb = locations[player-1][j]
                for x, y in valid_moves(board, marb, i+1):
                    boardc = board.copy()
                    move(boardc, marb[0], marb[1], x, y)
                    locationsc = locations.copy()
                    findAndReplaceMarb(locationsc, (marb, (x, y)), i+1)
                    evalu, next_move = minimax(boardc, depth - 1, True, alpha, beta, player, locationsc)
                    if evalu < min_eval :
                        min_move = (marb, (x, y))
                        min_eval = min(min_eval, evalu)
                        beta = min(beta, evalu)
                        if beta >= alpha:
                            break
        return min_eval, min_move