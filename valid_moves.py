#Checks moves with jumps
def check_jumps(board, node, player1, player2, moves):
    row, col = node
    length = len(board[0])
    width  = len(board[1])
    #If spot to the right is occupied and the spot after is empty
    if (col + 2 < width -1  and col + 4 < width -1): 
        if (board[row][col+2] == player1 or board[row][col+2] == player2) and (board[row][col+4] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row, col+4))
            check_jumps(jumpboard, (row, col+4), player1, player2, moves)
    #If spot to the left is occupied and the spot after is empty
    if (col - 2 >= 0 and col - 4 >= 0): 
        if (board[row][col-2] == player1 or board[row][col-2] == player2) and  (board[row][col-4] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row, col-4))
            check_jumps(jumpboard, (row, col-4), player1, player2, moves)
    #If spot to the top right is occupied and the spot after is empty
    if (row - 1 >= 0 and col + 1 < width - 1  and row - 2 >= 0 and col + 2 < width -1):
        if (board[row-1][col+1] == player1 or board[row-1][col+1] == player2) and  (board[row-2][col+2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row-2, col+2))
            check_jumps(jumpboard, (row-2, col+2), player1, player2, moves)
    #If spot to the top left is occupied and the spot after is empty
    if (row - 1 >= 0 and col - 1 >= 0  and row - 2 >= 0 and col - 2 >= 0):
        if (board[row-1][col-1] == player1 or board[row-1][col-1] == player2) and  (board[row-2][col-2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row-2, col-2))
            check_jumps(jumpboard, (row-2, col-2), player1, player2, moves)
    #If spot to the bottom left is occupied and the spot after is empty
    if (row + 1 < length - 1 and col - 1 >= 0  and row + 2 < length - 1 and col - 2 >= 0): 
        if (board[row+1][col-1] == player1 or board[row+1][col-1] == player2) and  (board[row+2][col-2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row+2, col-2))
            check_jumps(jumpboard, (row+2, col-2), player1, player2, moves)
    #If spot to the bottom right is occupied and the spot after is empty
    if (row + 1 < length - 1 and col + 1 < width -1  and row + 2 < length - 1 and col + 2 < width -1):
        if (board[row+1][col+1] == player1 or board[row+1][col+1] == player2) and  (board[row+2][col+2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row+2, col+2))
            check_jumps(jumpboard, (row+2, col+2), player1, player2, moves)

#Determines the valid moves from the given node
#Board - the board
#node - the place you want to move from
#player1 - number of player making the move
#player2 - number of other player in the game
def valid_moves(board, node, player1, player2):
    #moves is a array of tuples representing locations on the board you can move to
    moves = []
    
    row,col = node
    
    length = len(board[0])
    width = len(board[1])
    
    #Checking if you can move one to the right
    if (col + 2 < width -1):
        if board[row][col+2] == 0:
            moves.append((row, col+2))
    #Checking if you can move one to the left
    if (col - 2 >= 0):
        if board[row][col-2] == 0:
            moves.append((row, col-2))
    #Checking if you can move up left
    if (row - 1 >= 0 and col - 1 >= 0):
        if board[row-1][col-1] == 0:
            moves.append((row-1, col-1))
    #Checking if you can move up right
    if (row - 1 >= 0 and col + 1 < width -1):
        if board[row-1][col+1] == 0:
            moves.append((row-1, col+1))
    #Checking if you can move down left
    if (row + 1 < length - 1 and col - 1  >= 0):
        if board[row+1][col-1] == 0:
            moves.append((row+1, col-1))
    #Checking if you can move down right
    if (row + 1 < length - 1 and col + 1 < width -1):
        if board[row+1][col+1] == 0:
            moves.append((row+1, col+1))
        
    #Checking for jumps
    #Adds each possible move on a link of jumps
    
    #If spot to the right is occupied and the spot after is empty
    if (col + 2 < width -1  and col + 4 < width -1): 
        if (board[row][col+2] == player1 or board[row][col+2] == player2) and (board[row][col+4] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row, col+4))
            check_jumps(jumpboard, (row, col+4), player1, player2, moves)
    #If spot to the left is occupied and the spot after is empty
    if (col - 2 >= 0 and col - 4 >= 0): 
        if (board[row][col-2] == player1 or board[row][col-2] == player2) and  (board[row][col-4] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row, col-4))
            check_jumps(jumpboard, (row, col-4), player1, player2, moves)
    #If spot to the top right is occupied and the spot after is empty
    if (row - 1 >= 0 and col + 1 < width - 1  and row - 2 >= 0 and col + 2 < width -1):
        if (board[row-1][col+1] == player1 or board[row-1][col+1] == player2) and  (board[row-2][col+2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row-2, col+2))
            check_jumps(jumpboard, (row-2, col+2), player1, player2, moves)
    #If spot to the top left is occupied and the spot after is empty
    if (row - 1 >= 0 and col - 1 >= 0  and row - 2 >= 0 and col - 2 >= 0):
        if (board[row-1][col-1] == player1 or board[row-1][col-1] == player2) and  (board[row-2][col-2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row-2, col-2))
            check_jumps(jumpboard, (row-2, col-2), player1, player2, moves)
    #If spot to the bottom left is occupied and the spot after is empty
    if (row + 1 < length - 1 and col - 1 >= 0  and row + 2 < length - 1 and col - 2 >= 0): 
        if (board[row+1][col-1] == player1 or board[row+1][col-1] == player2) and  (board[row+2][col-2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row+2, col-2))
            check_jumps(jumpboard, (row+2, col-2), player1, player2, moves)
    #If spot to the bottom right is occupied and the spot after is empty
    if (row + 1 < length - 1 and col + 1 < width -1  and row + 2 < length - 1 and col + 2 < width -1):
        if (board[row+1][col+1] == player1 or board[row+1][col+1] == player2) and  (board[row+2][col+2] == 0):
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row+2, col+2))
            check_jumps(jumpboard, (row+2, col+2), player1, player2, moves)

    return moves
    