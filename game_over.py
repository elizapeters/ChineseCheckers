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

# determine if all on other side
def check_opposite(board, player):
    if player == 1:  # Player 1 should reach the bottom side
        return np.all(board[12:] == player)
    elif player == 2:
        return check_base_5(board, [9, 10, 11, 12])
    elif player == 3:
        return check_base_4(board, [9, 10, 11, 12])
    elif player == 4:
        return check_base_3(board, [7, 6, 5, 4])
    elif player == 5:
        return check_base_2(board, [7, 6, 5, 4])
    elif player == 6:  # Player 6 should reach the top side
        return np.all(board[:5] == player)

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
        if check_opposite(board, player):
            return True, f"Player {player} wins!"
    # Check for players with no valid moves left
    no_valid_moves_players = [player for player in players if no_valid_moves_left(board, player)]
    
    # If all players have no valid moves left, no one wins (draw)
    if len(no_valid_moves_players) == len(players):
        return True, "It's a draw!"
    return False, None
