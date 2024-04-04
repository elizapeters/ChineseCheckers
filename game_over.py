import numpy as np
from valid_moves import *

# def check_base_2(board, array):
#     times = 0 
#     for i in array:
#         if(i%2 == 0):
#             for j in range(1, times+1, 2):
#                 if(board[i][3-j] != 2 or board[i][3+j] != 2):
#                     return False
#         else:
#             for j in range(0, times+1, 2):
#                 if(board[i][3-j] != 2 or board[i][3+j] != 2):
#                     return False

# def check_base_3(board, array):
#     times = 0 
#     for i in array:
#         if(i%2 == 0):
#             for j in range(1, times+1, 2):
#                 if(board[i][21-j] != 3 or board[i][21+j] != 3):
#                     return False
#         else:
#             for j in range(0, times+1, 2):
#                 if(board[i][21-j] != 3 or board[i][21+j] != 3):
#                     return False    

# def check_base_4(board, array):
#     times = 0 
#     for i in array:
#         if(i%2 == 0):
#             for j in range(1, times+1, 2):
#                 if(board[i][3-j] != 2 or board[i][3+j] != 2):
#                     return False
#         else:
#             for j in range(0, times+1, 2):
#                 if(board[i][3-j] != 2 or board[i][3+j] != 2):
#                     return False
                
# def check_base_5(board, array):
#     times = 0 
#     for i in array:
#         if(i%2 == 0):
#             for j in range(1, times+1, 2):
#                 if(board[i][21-j] != 3 or board[i][21+j] != 3):
#                     return False
#         else:
#             for j in range(0, times+1, 2):
#                 if(board[i][21-j] != 3 or board[i][21+j] != 3):
#                     return False          

# # determine if all on other side
# def check_opposite(board, player):
#     if player == 1:  # Player 1 should reach the bottom side
#         return np.all(board[12:] == player)
#     elif player == 2:
#         return check_base_5(board, [9, 10, 11, 12])
#     elif player == 3:
#         return check_base_4(board, [9, 10, 11, 12])
#     elif player == 4:
#         return check_base_3(board, [7, 6, 5, 4])
#     elif player == 5:
#         return check_base_2(board, [7, 6, 5, 4])
#     elif player == 6:  # Player 6 should reach the top side
#         return np.all(board[:5] == player)

# def no_valid_moves_left(board, player, opponent):
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == player:
#                 if valid_moves(board, (i, j), player, opponent):
#                     return False
#     print(f"Player {player} has no valid moves left.")
#     return True


# def game_over(board, players):
#     for player in players:
#         if check_opposite(board, player):
#             return True, f"Player {player} wins!"
#     for player in players:
#         opponent = [p for p in players if p != player][0]
#         if no_valid_moves_left(board, player, opponent):
#             return True, f"Player {opponent} wins!"
#     return False, None

def check_top_bottom(board, array, val):
    times = 0
    for i in array:
        if(i%2 == 0):
            for j in range(0, times+1, 2):
                if (board[i][12-j] != val or board[i][12+j] != val):
                    return False
        else:
            for j in range(1, times+1, 2):
                if (board[i][12-j] != val or board[i][12+j] != val):
                    return False
        times = times+1
    return True

def check_middleTri_second(board, array, firstVal, secondVal):
    times = 0
    for i in array:
        minFill = 3
        maxfill = 21
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                if (board[i][21-j] != secondVal or board[i][21+j] != secondVal):
                    return False
                maxfill = 21-j-2
        else:
            for j in range(0, times+1, 2):
                if (board[i][21-j] != secondVal or board[i][21+j] != secondVal):
                    return False 
                maxfill = 21-j-2
        times = times+1
    return True

def check_middleTri_first(board, array, firstVal, secondVal):
    times = 0
    for i in array:
        minFill = 3
        maxfill = 21
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                if (board[i][3-j] != firstVal or board[i][3+j] != firstVal):
                    return False
                minFill = 3+j +2
        else:
            for j in range(0, times+1, 2):
                if (board[i][3+j] != firstVal or board[i][3-j] != firstVal):
                    return False
                minFill = 3+j +2
        times = times+1
    return True


def game_over(board):
    check = check_top_bottom(board, [0,1,2,3], 6) or check_top_bottom(board, [16,15,14,13], 1) or check_middleTri_first(board, [7, 6, 5, 4], 5, 4) or check_middleTri_first(board, [9, 10, 11, 12], 3, 2) or check_middleTri_second(board, [7, 6, 5, 4], 5, 4) or check_middleTri_second(board, [9, 10, 11, 12], 3, 2)
    first_check = check or check_middleTri_first(board, [7, 6, 5, 4], 5, 4) or check_middleTri_first(board, [9, 10, 11, 12], 3, 2)
    second_check = check_middleTri_second(board, [7, 6, 5, 4], 5, 4) or check_middleTri_second(board, [9, 10, 11, 12], 3, 2)
    return check