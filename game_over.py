import numpy as np
from valid_moves import *

# determine if all on other side
def check_opposite(board, player):
    if player == 1:  # Player 1 should reach the bottom side
        return np.all(board[12:] == player)
    elif player == 6:  # Player 6 should reach the top side
        return np.all(board[:5] == player)

def no_valid_moves_left(board, player, opponent):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                if valid_moves(board, (i, j), player, opponent):
                    return False
    print(f"Player {player} has no valid moves left.")
    return True


def game_over(board, player1, player2):
    if check_opposite(board, player1):
        return True, f"Player {player1} wins!"
    elif check_opposite(board, player2):
        return True, f"Player {player2} wins!"
    if no_valid_moves_left(board, player1, player2):
        return True, f"Player {player2} wins!"
    elif no_valid_moves_left(board, player2, player1):
        return True, f"Player {player1} wins!"
    
    return False, None
