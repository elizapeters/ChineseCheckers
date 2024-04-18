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

base_nodes_rank_reverse = [[(3, 15), (3, 13), (3, 11), (3, 9), (2, 14), (2, 12), (2, 10), (1, 13), (1, 11), (0, 12)],
[(4, 6), (5, 5), (6, 4), (7, 3), (4, 4), (5, 3), (6, 2), (4, 2), (5, 1), (4, 0)],
[(7, 21), (6, 20), (5, 19), (4, 18), (6, 22), (5, 21), (4, 20), (5, 23), (4, 22), (4, 24)],
[(12, 6), (11, 5), (10, 4), (9, 3), (12, 4), (11, 3), (10, 2), (12, 2), (11, 1), (12, 0)],
[(9, 21), (10, 20), (11, 19), (12, 18), (10, 22), (11, 21), (12, 20), (11, 23), (12, 22), (12, 24)],
[(13, 15), (13, 13), (13, 11), (13, 9), (14, 14), (14, 12), (14, 10), (15, 13), (15, 11), (16, 12)]]

# returns the nodes in the triangle that are frozen
def find_frozen_nodes(board, player):
    frozen_nodes = []
    opponents = [5,4,3,2,1,0]
    opponent = opponents[player-1]
    for n in base_nodes_rank[opponent]:
        if (board[n] != player):
            return frozen_nodes
        frozen_nodes.append(n)
    return frozen_nodes
    
# get the farthest back node that is not taken by a marble
def get_goal_node(board, player):
    opponents = [5,4,3,2,1,0]
    opponent = opponents[player-1]
    goal_node = base_nodes_rank_reverse[opponent][9]
    for node in base_nodes_rank_reverse[opponent]:
        if board[node] != player:
            goal_node = node
    return goal_node

def distance_to_goal_node(goal, current):
    x1, y1 = goal
    x2, y2 = current
    return math.sqrt(((x2 - x1)) ** 2 + (y2 - y1) ** 2)

# get the total distance for each marble to the goal node
def calculate_distance(board, player, goal_node):
    total_distance = 0
    for i in range(len(board)):
            for j in range(len(board[0])):
                cell = (i,j)
                if (board[cell] == player):
                    distance = distance_to_goal_node(goal_node, cell)
                    total_distance += distance
    return total_distance

# find the move that minimizes the total distance
def best_move(board, all_moves, player):
    distance_list = []
    goal_node = get_goal_node(board, player)
    board_copy = board.copy()
    frozen_nodes = find_frozen_nodes(board, player)
    all_moves = [pair for pair in all_moves if not frozen_nodes.__contains__(pair[0])]
    
    for pairing in all_moves:
        start_node = pairing[0]
        end_node = pairing[1]
        boardcc = board_copy.copy()
        move(boardcc, start_node[0], start_node[1], end_node[0], end_node[1])
        updated_distance = calculate_distance(boardcc, player, goal_node)
        distance_list.append(updated_distance)
    min_index = distance_list.index(min(distance_list))
    opt_pairing = all_moves[min_index]
    opt_starting_node = opt_pairing[0]
    opt_ending_node = opt_pairing[1]
    return opt_starting_node, opt_ending_node
