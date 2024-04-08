from valid_moves import *
from game_initialization import *
from game_over import *
from move import *
import math

base_nodes_rank = [[(0,12),(1,11),(1,13),(2,10),(2,12),(2,14),(3,9),(3,11),(3,13),(3,15)], # done #player 1 goal
              [(4,0),(5,1),(4,2),(6,2),(5,3),(4,4),(7,3),(6,4),(5,5),(4,6)], #done player 2
              [(4,24),(4,22),(5,23),(4,20),(5,21),(6,22),(4,18),(5,19),(6,20),(7,21)], # done
              [(12,0),(11,1),(12,2),(10,2),(11,3),(12,4),(9,3),(10,4),(11,5),(12,6)], #done
              [(12,24),(12,22),(11,23),(12,20),(11,21),(10,22),(12,18),(11,19),(10,20),(9,21)], #done 
              [(16,12),(15,11),(15,13),(14,10),(14,12),(14,14),(13,9),(13,11),(13,13),(13,15)]] #done

opponents = [5,4,3,2,1,0]


def distance_to_goal_node(goal, current):
    x1, y1 = goal
    x2, y2 = current
    return math.sqrt(((x2 - x1)/2) ** 2 + (y2 - y1) ** 2)

def calculate_distance(board, player):
    goal_node_list = [(16,12),(12,24),(12,0),(4,24),(4,0),(0,12)]
    goal_node = goal_node_list[player-1]
    
    opponent = opponents[player-1]
    i = 1
    while board[goal_node] == player and i < len(base_nodes_rank[0]):
        goal_node = base_nodes_rank[opponent][i]
        i += 1
    
    total_distance = 0
    for i in range(len(board)):
            for j in range(len(board[0])):
                cell = (i,j)
                if (board[cell] == player):
                    distance = distance_to_goal_node(goal_node, cell)
                    total_distance += distance

    return total_distance

def get_best_move(board, moves, current, player):
    print("getting best move from", current, "player", player)
    board_copy = board.copy()
    potential_move_distances = []
    for valid_move in moves:
        print("hitting a valid move")
        boardcc = board_copy.copy()
        move(boardcc, current[0], current[1], valid_move[0], valid_move[1])
        updated_distance = calculate_distance(boardcc, player)
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
        boardcc = board_copy.copy()
        key_list.append(key)
        move(boardcc, key[0], key[1], val[0], val[1])
        updated_distance = calculate_distance(boardcc, playerturn)
        distance_list.append(updated_distance)

    min_index = distance_list.index(min(distance_list))
    opt_starting_node = key_list[min_index]
    opt_ending_node = dictionary[opt_starting_node]
    return opt_starting_node, opt_ending_node

