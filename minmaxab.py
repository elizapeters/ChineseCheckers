from valid_moves import *
from game_initialization import *
from game_over import *
from move import *
import math
from greedy import *
import random
import copy

def findAndReplaceMarb(locations, opter, player):
    for i in range(len(locations[player-1])):
        marb = locations[player-1][i]
        if marb[0] == opter[0][0] and marb[1] == opter[0][1]:
            locations[player-1][i] = (opter[1][0], opter[1][1])
            return


def findAllMoves(board, locations, player):
    goal_node = get_goal_node(board, player)
    return_list = []
    for i in range(10):
        x, y = locations[player][i]
        possible_moves = valid_moves(board, (x, y), player)
        for one_move in possible_moves:
            return_list.append(((x, y), (one_move[0], one_move[1])))
        frozen_nodes = find_frozen_nodes(board, player)
        return_list = [pair for pair in return_list if not frozen_nodes.__contains__(pair[0])]
    return_list.sort(key=lambda item: distance_to_goal_node(goal_node, (item[1][0], item[1][1])))
    return_list = return_list[:2]
    return return_list

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
        all_players_all_moves = []
        for p in range(len(locations)):
            if(p != player-1):
                all_players_all_moves.append(findAllMoves(board, locations, p))
        min_eval = float('inf')
        min_move = (0, 0, 0, 0)
        for first in all_players_all_moves[0]:
            for second in all_players_all_moves[1]:
                for third in all_players_all_moves[2]:
                    for fourth in all_players_all_moves[3]:
                        for fifth in all_players_all_moves[4]:
                            boardc = board.copy()
                            locationsc = copy.deepcopy(locations)
                            move(boardc, first[0][0], first[0][1], first[1][0], first[1][1])
                            move(boardc, second[0][0], second[0][1], second[1][0], second[1][1])
                            move(boardc, third[0][0], third[0][1], third[1][0], third[1][1])
                            move(boardc, fourth[0][0], fourth[0][1], fourth[1][0], fourth[1][1])
                            move(boardc, fourth[0][0], fourth[0][1], fourth[1][0], fourth[1][1])
                            findAndReplaceMarb(locationsc, ((first[0][0], first[0][1]), (first[1][0], first[1][1])), boardc[first[1][0]][first[1][1]])
                            findAndReplaceMarb(locationsc, ((second[0][0], second[0][1]), (second[1][0], second[1][1])), boardc[second[1][0]][second[1][1]])
                            findAndReplaceMarb(locationsc, ((third[0][0], third[0][1]), (third[1][0], third[1][1])), boardc[third[1][0]][third[1][1]])
                            findAndReplaceMarb(locationsc, ((fourth[0][0], fourth[0][1]), (fourth[1][0], fourth[1][1])), boardc[fourth[1][0]][fourth[1][1]])
                            findAndReplaceMarb(locationsc, ((fifth[0][0], fifth[0][1]), (fifth[1][0], fifth[1][1])), boardc[fifth[1][0]][fifth[1][1]])
                            evalu, next_move = minimax(boardc, depth - 1, True, alpha, beta, player, locationsc, get_goal_node(board, player))
                            if evalu < min_eval :
                                min_move = next_move
                                min_eval = min(min_eval, evalu)
                                beta = min(beta, evalu)
                        if beta >= alpha:
                            break
                    if beta >= alpha:
                        break
        return min_eval, min_move