from valid_moves import *
from game_initialization import *
from game_over import *
from move import *
import math
from minimax import *
import random
import copy

def findAndReplaceMarb(locations, opter, player):
    for i in range(len(locations[player-1])):
        marb = locations[player-1][i]
        if marb[0] == opter[0][0] and marb[1] == opter[0][1]:
            locations[player-1][i] = (opter[1][0], opter[1][1])
            return



# Minimax with Alpha-Beta pruning
def minimax(board, depth, maximizing_player, alpha, beta, player, locations, prev_goal_node):
    if depth == 0 or game_over(board):
        return -1*calculate_distance(board, player, prev_goal_node), (0,0,0,0)

    if maximizing_player:
        all_moves = []
        for i in range(len(locations[player-1])):
            x, y = locations[player-1][i]
            possible_moves = valid_moves(board, (x, y), player)
            for one_move in possible_moves:
                all_moves.append(((x, y), (one_move[0], one_move[1])))

        frozen_nodes = find_frozen_nodes(board, player)
        all_moves = [pair for pair in all_moves if not frozen_nodes.__contains__(pair[0])]
        max_eval = float('-inf')
        max_move = all_moves[0]
        distance_list = []
        goal_node = get_goal_node(board, player)
        board_copy = board.copy()
        for pairing in all_moves:
            start_node = pairing[0]
            end_node = pairing[1]
            boardcc = board_copy.copy()
            move(boardcc, start_node[0], start_node[1], end_node[0], end_node[1])
            locationsc = copy.deepcopy(locations)
            findAndReplaceMarb(locationsc, ((start_node[0], start_node[1]), (end_node[0], end_node[1])), player)
            evalu, next_move = minimax(boardcc, depth - 1, False, alpha, beta, player, locationsc, get_goal_node(board, player))
            if evalu > max_eval :
                max_move = ((start_node[0], start_node[1]), (end_node[0], end_node[1]))
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
                        locationsc = copy.deepcopy(locations)
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