import numpy as np

def topAndBottom(board, array, currentVal):
    times = 0
    for i in array:
        if(i%2 == 0):
            for j in range(0, times+1, 2):
                board[i][12-j] = currentVal
                board[i][12+j] = currentVal
        else:
            for j in range(1, times+1, 2):
                board[i][12-j] = currentVal
                board[i][12+j] = currentVal
        times = times+1

def middleTri(board, array, firstVal, secondVal):
    times = 0
    for i in array:
        minFill = 3
        maxfill = 21
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                board[i][3-j] = firstVal
                board[i][3+j] = firstVal
                minFill = 3+j +2
        else:
            for j in range(0, times+1, 2):
                board[i][3-j] = firstVal
                board[i][3+j] = firstVal
                minFill = 3+j +2
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                board[i][21-j] = secondVal
                board[i][21+j] = secondVal
                maxfill = 21-j-2
        else:
            for j in range(0, times+1, 2):
                board[i][21-j] = secondVal
                board[i][21+j] = secondVal
                maxfill = 21-j-2
        for j in range(minFill, maxfill+1, 2):
            board[i][j] = 0
        times = times+1


def spaces(board):
    for i in range(4, 21, 2):
        board[8][i] = 0


def boardBuilder():
    board = np.ones((17,25), dtype=int)*-1
    topAndBottom(board, [0, 1, 2, 3], 1)
    topAndBottom(board, [16, 15, 14, 13], 6)
    middleTri(board, [7, 6, 5, 4], 2, 3)
    middleTri(board, [9, 10, 11, 12], 4, 5)
    spaces(board)
    return board

board = boardBuilder()
print(board)

