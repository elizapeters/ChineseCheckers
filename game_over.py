import numpy as np
from valid_moves import *
 
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