from valid_moves import *
from game_initialization import *
from game_over import *
from move import *
import math
from minimax import *
import random

def findAndReplaceMarb(locations, optMove, player):
    for i in range(len(locations[player-1])):
        marb = locations[player-1][i]
        if marb[0] == optMove[0][0] and marb[1] == optMove[0][1]:
            locations[player-1][i] = optMove[1]



# Minimax with Alpha-Beta pruning
def minimax(board, depth, maximizing_player, alpha, beta, player, locations):
    if depth == 0 or game_over(board):
        goal_node = get_goal_node(board, player)
        return -1* calculate_distance(board, player, goal_node), (0,0,0,0)

    if maximizing_player:
        all_moves = []
        max_eval = float('-inf')
        max_move = ((0, 0), (0, 0))
        for i in range(len(locations[player-1])):
            marb = locations[player-1][i]
            possible_moves = valid_moves(board, marb, player)
            for one_move in possible_moves:
                all_moves.append(((locations[player-1][i][0], locations[player-1][i][1]), one_move))

        random.shuffle(all_moves)
        frozen_nodes = find_frozen_nodes(board, player)
        all_moves = [pair for pair in all_moves if not frozen_nodes.__contains__(pair[0])]
        for start, end in all_moves: 
            boardc = board.copy()
            move(boardc, start[0], start[1], end[0], end[1])
            locationsc = locations.copy()
            findAndReplaceMarb(locationsc, (start, end), player)
            evalu, next_move = minimax(boardc, depth - 1, False, alpha, beta, player, locationsc)
            if evalu > max_eval :
                max_move = (start, end)
                max_eval = evalu
                alpha = evalu
            if beta <= alpha:
                break
        return max_eval, max_move
    else:
        min_eval = float('inf')
        min_move = (0, 0, 0, 0)
        for i in range(len(locations)):
            if i != player-1:
                for j in range(len(locations[i])):
                    marb = locations[i][j]
                    pos_moves = valid_moves(board, marb, i+1)
                    frozen_nodes = find_frozen_nodes(board, i+1)
                    all_moves = [pair for pair in pos_moves if not frozen_nodes.__contains__(pair)]
                    for x, y in all_moves:
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
                    if beta >= alpha:
                        break
        return min_eval, min_move