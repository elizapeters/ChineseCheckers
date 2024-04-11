import numpy as np

def topAndBottom(board, array, currentVal, starting_spots):
    index = 0
    times = 0
    for i in array:
        if(i%2 == 0):
            for j in range(0, times+1, 2):
               # print("what",currentVal)
                board[i][12-j] = currentVal
                board[i][12+j] = currentVal
                if j == 0:
                    starting_spots[currentVal-1][index] = (i, 12)
                    index = index +1
                else:
                    starting_spots[currentVal-1][index] = (i, 12-j)
                    index = index +1
                    starting_spots[currentVal-1][index] = (i, 12+j)
                    index = index +1
        else:
            for j in range(1, times+1, 2):
               # print("this", currentVal)
                board[i][12-j] = currentVal
                board[i][12+j] = currentVal
                starting_spots[currentVal-1][index] = (i, 12-j)
                index = index +1
                starting_spots[currentVal-1][index] = (i, 12+j)
                index = index +1
        times = times+1

def middleTri(board, array, firstVal, secondVal, starting_spots):
    times = 0
    index1 = 0
    index2 = 0
    for i in array:
        minFill = 3
        maxfill = 21
        if(i%2 == 0):
            for j in range(1, times+1, 2):
                #firstVal
                board[i][3-j] = firstVal
                board[i][3+j] = firstVal
                minFill = 3+j +2
                #SecondVal
                board[i][21-j] = secondVal
                board[i][21+j] = secondVal
                maxfill = 21-j-2
                if j == 0:
                    starting_spots[firstVal-1][index1] = (i, 3)
                    starting_spots[secondVal-1][index2] = (i, 21)
                    index1 = index1 +1 
                    index2 = index2 +1
                else :
                    starting_spots[firstVal-1][index1] = (i, 3-j)
                    index1 = index1 +1
                    starting_spots[firstVal-1][index1] = (i, 3+j)
                    index1 = index1 +1
                    starting_spots[secondVal-1][index2] = (i, 21-j)
                    index2 = index2 +1
                    starting_spots[secondVal-1][index2] = (i, 21+j)
                    index2 = index2 +1
        else:
            for j in range(0, times+1, 2):
                #first val
                board[i][3-j] = firstVal
                board[i][3+j] = firstVal
                minFill = 3+j +2
                #second val
                board[i][21-j] = secondVal
                board[i][21+j] = secondVal
                maxfill = 21-j-2

                if j == 0:
                    starting_spots[firstVal-1][index1] = (i, 3)
                    starting_spots[secondVal-1][index2] = (i, 21-j)
                    index1 = index1 +1 
                    index2 = index2 +1
                else :
                    starting_spots[firstVal-1][index1] = (i, 3-j)
                    index1 = index1 +1
                    starting_spots[firstVal-1][index1] = (i, 3+j)
                    index1 = index1 +1
                    starting_spots[secondVal-1][index2] = (i, 21-j)
                    index2 = index2 +1
                    starting_spots[secondVal-1][index2] = (i, 21+j)
                    index2 = index2 +1
                
        for j in range(minFill, maxfill+1, 2):
            board[i][j] = 0
        times = times+1


def spaces(board):
    for i in range(4, 21, 2):
        board[8][i] = 0


def boardBuilder():
    board = np.ones((17,25), dtype=int)*-1
    starting_spots = np.ones((6,10, 2), dtype=int)*-1
    topAndBottom(board, [0, 1, 2, 3], 1, starting_spots)
    topAndBottom(board, [16, 15, 14, 13], 6, starting_spots)
    middleTri(board, [7, 6, 5, 4], 2, 3, starting_spots)
    middleTri(board, [9, 10, 11, 12], 4, 5, starting_spots)
    spaces(board)
    return board, starting_spots

board = boardBuilder()
#print(board)

