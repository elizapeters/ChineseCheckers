import numpy as np
from valid_moves import *

def check_base_2(board, array):
    times = 0 
    for i in array:
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                if(board[i][3-j] != 2 or board[i][3+j] != 2):
                    return False
        else:
            for j in range(0, times+1, 2):
                if(board[i][3-j] != 2 or board[i][3+j] != 2):
                    return False
    return True

def check_base_3(board, array):
    times = 0 
    for i in array:
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                if(board[i][21-j] != 3 or board[i][21+j] != 3):
                    return False
        else:
            for j in range(0, times+1, 2):
                if(board[i][21-j] != 3 or board[i][21+j] != 3):
                    return False 
    return True   

def check_base_4(board, array):
    times = 0 
    for i in array:
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                if(board[i][3-j] != 2 or board[i][3+j] != 2):
                    return False
        else:
            for j in range(0, times+1, 2):
                if(board[i][3-j] != 2 or board[i][3+j] != 2):
                    return False
    return True
                
def check_base_5(board, array):
    times = 0 
    for i in array:
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                if(board[i][21-j] != 3 or board[i][21+j] != 3):
                    return False
        else:
            for j in range(0, times+1, 2):
                if(board[i][21-j] != 3 or board[i][21+j] != 3):
                    return False   
    return True       

# determine if all on other side
def check_opposite(board, player):
    if player == 1:  # Player 1 should reach the bottom side
        return np.all(board[12:] == player)
    elif player == 2:
        return np.all(check_base_5(board, [9, 10, 11, 12]))
    elif player == 3:
        return np.all(check_base_4(board, [9, 10, 11, 12]))
    elif player == 4:
        return np.all(check_base_3(board, [7, 6, 5, 4]))
    elif player == 5:
        return np.all(check_base_2(board, [7, 6, 5, 4]))
    elif player == 6:  # Player 6 should reach the top side
        return np.all(board[:5] == player)
    
base_nodes = [[(0,12),(1,11),(1,13),(2,10),(2,12),(2,14),(3,9),(3,11),(3,13),(3,15)],
              [(7,3),(6,2),(6,4),(5,1),(5,3),(5,5),(4,0),(4,2),(4,4),(4,6)],
              [(7,21),(6,20),(6,22),(5,19),(5,21),(5,23),(4,18),(4,20),(4,22),(4,24)],
              [(9,3),(10,2),(10,4),(11,1),(11,3),(11,5),(12,0),(12,2),(12,4),(12,6)],
              [(9,21),(10,20),(10,22),(11,19),(11,21),(11,23),(12,18),(12,20),(12,22),(12,24)],
              [(16,12),(15,11),(15,13),(14,10),(14,12),(14,14),(13,9),(13,11),(13,13),(13,15)]]

opponents = [5,4,3,2,1,0]

def oppo(player, opponent):
    player_base_nodes = base_nodes[player - 1]
    opponent_base_nodes = base_nodes[opponent]
    
    # Check if all player's marbles are in the opposing player's base nodes
    for player_marble in player_base_nodes:
        if player_marble not in opponent_base_nodes:
            return False
    
    return True 


def no_valid_moves_left(board, player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                if valid_moves(board, (i, j), player):
                    return False
    print(f"Player {player} has no valid moves left.")
    return True


def game_over(board, players):
    for player in players:
        if oppo(board, player):
            return True, f"Player {player} wins!"
    # for player in players:
    #     if check_opposite(board, player):
    #         return True, f"Player {player} wins!"
    # # Check for players with no valid moves left
    # no_valid_moves_players = [player for player in players if no_valid_moves_left(board, player)]
    
    # # If all players have no valid moves left, no one wins (draw)
    # if len(no_valid_moves_players) == len(players):
    #     return True, "It's a draw!"
    return False, None
