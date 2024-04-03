from valid_moves import *
from game_initialization import *
from game_over import *
from move import *
import math

def distance_to_goal_node(goal, current):
    x1, y1 = goal
    x2, y2 = current
    return math.sqrt(((x2 - x1)/2) ** 2 + (y2 - y1) ** 2)

def calculate_distance(board, player):
    goal_node_list = [(16,12),(12,24),(12,0),(4,24),(4,0),(0,12)]
    goal_node = goal_node_list[player-1]
    total_distance = 0
    for i, row in enumerate(board):
            for j, cell in enumerate(row):
                cell = (i,j)
                if (cell == player):
                    distance = distance_to_goal_node(goal_node, cell)
                    print("distance for single node to goal node", distance)
                    total_distance += distance

    return total_distance

def get_best_move(board, moves, current, player):
    print("getting best move from", current, "player", player)
    board_copy = board.copy()
    potential_move_distances = []
    for valid_move in moves:
        print("hitting a valid move")
        board = board_copy.copy()
        move(board, current[0], current[1], valid_move[0], valid_move[1])
        updated_distance = calculate_distance(board, player)
        potential_move_distances.append(updated_distance)

    if not potential_move_distances:
        return None
    print("list", potential_move_distances)
    min_index = potential_move_distances.index(min(potential_move_distances))
    best_move = moves[min_index]
    # get the index of the min in potential omve distances
    # return the corresponding move fro moves
    # this function returns the best slot that the selected marble should go tom
    return best_move

def best_of_best(board, dictionary, playerturn):
    distance_list = []
    key_list = []
    board_copy = board.copy()
    # loops through every possible move combo
    for key in dictionary:
        val = dictionary[key]
        board = board_copy.copy()
        key_list.append(key)
        move(board, key[0], key[1], val[0], val[1])
        updated_distance = calculate_distance(board, playerturn)
        distance_list.append(updated_distance)

    min_index = distance_list.index(min(distance_list))
    opt_starting_node = key_list[min_index]
    opt_ending_node = dictionary[opt_starting_node]
    return opt_starting_node, opt_ending_node

