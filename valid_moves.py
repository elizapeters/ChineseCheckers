base_nodes = [[(0,12),(1,11),(1,13),(2,10),(2,12),(2,14),(3,9),(3,11),(3,13),(3,15)],
              [(7,3),(6,2),(6,4),(5,1),(5,3),(5,5),(4,0),(4,2),(4,4),(4,6)],
              [(7,21),(6,20),(6,22),(5,19),(5,21),(5,23),(4,18),(4,20),(4,22),(4,24)],
              [(9,3),(10,2),(10,4),(11,1),(11,3),(11,5),(12,0),(12,2),(12,4),(12,6)],
              [(9,21),(10,20),(10,22),(11,19),(11,21),(11,23),(12,18),(12,20),(12,22),(12,24)],
              [(16,12),(15,11),(15,13),(14,10),(14,12),(14,14),(13,9),(13,11),(13,13),(13,15)]]

opponents = [5,4,3,2,1,0]

def valid_space(player1, opponent, node):
    for i in range(len(base_nodes)):
                    if i != player1-1 and i != opponent:
                        for base_node in base_nodes[i]:
                            row, col = base_node
                            curr_row, curr_col = node
                            if curr_row == row and curr_col == col:
                               return False
    return True    

def check_jumps(board, node, player1, moves, opponent, length, width):
    row, col = node
    #If it is 0, then move
    #and if not part of the other bases that is not you or your opponent
    
    #If spot to the right is occupied and the spot after is empty
    if (col + 2 < width  and col + 4 < width): 
        next_node = board[row][col+4]
        if (board[row][col+2] > 0 and board[row][col+2] < 7 and next_node == 0 and valid_space(player1, opponent, (row, col+4))):  
            jumpboard = board.copy()
            #This is so in the recursion there isn't an infinte loop of jumping back and forth
            jumpboard[row][col] = -1
            moves.append((row, col+4))
            check_jumps(jumpboard, (row, col+4), player1, moves, opponent, length, width)
    #If spot to the left is occupied and the spot after is empty
    if (col - 2 >= 0 and col - 4 >= 0): 
        next_node = board[row][col-4]
        if (board[row][col-2] > 0 and board[row][col-2] < 7 and next_node == 0 and valid_space(player1, opponent, (row, col-4))):
            jumpboard = board.copy()
            jumpboard[row][col] = -1
            moves.append((row, col-4))
            check_jumps(jumpboard, (row, col-4), player1, moves, opponent, length, width)
    #If spot to the top right is occupied and the spot after is empty
    if (row - 1 >= 0 and col + 1 < width   and row - 2 >= 0 and col + 2 < width):
        next_node = board[row-2][col+2]
        if (board[row-1][col+1] > 0 and board[row-1][col+1] < 7 and next_node == 0 and valid_space(player1, opponent, (row-2, col+2))):
            jumpboard = board.copy()
            jumpboard[row][col] = -1
            moves.append((row-2, col+2))
            check_jumps(jumpboard, (row-2, col+2), player1, moves, opponent, length, width)
    #If spot to the top left is occupied and the spot after is empty
    if (row - 1 >= 0 and col - 1 >= 0  and row - 2 >= 0 and col - 2 >= 0):
        next_node = board[row-2][col-2]
        if (board[row-1][col-1] > 0 and board[row-1][col-1] < 7 and next_node == 0 and valid_space(player1, opponent, (row-2, col-2))):
            jumpboard = board.copy()
            jumpboard[row][col] = -1
            moves.append((row-2, col-2))
            check_jumps(jumpboard, (row-2, col-2), player1, moves, opponent, length, width)
    #If spot to the bottom left is occupied and the spot after is empty
    if (row + 1 < length and col - 1 >= 0  and row + 2 < length and col - 2 >= 0): 
        next_node = board[row+2][col-2]
        if (board[row+1][col-1] > 0 and board[row+1][col-1] < 7 and next_node == 0 and valid_space(player1, opponent, (row+2, col-2))):
            jumpboard = board.copy()
            jumpboard[row][col] = -1
            moves.append((row+2, col-2))
            check_jumps(jumpboard, (row+2, col-2), player1, moves, opponent, length, width)
    #If spot to the bottom right is occupied and the spot after is empty
    if (row + 1 < length and col + 1 < width   and row + 2 < length and col + 2 < width):
        next_node = board[row+2][col+2]
        if (board[row+1][col+1] > 0 and board[row+1][col+1] < 7 and next_node == 0 and valid_space(player1, opponent, (row+2, col+2))):
            jumpboard = board.copy()
            jumpboard[row][col] = -1
            moves.append((row+2, col+2))
            check_jumps(jumpboard, (row+2, col+2), player1, moves, opponent, length, width)

#Determines the valid moves from the given node
#Board - the board
#node - the place you want to move from
#player1 - number of player making the move
def valid_moves(board, node, player1):
    #moves is a array of tuples representing locations on the board you can move to
    moves = []
    
    row,col = node
    
    length = len(board)
    width = len(board[1])
    
    opponent = opponents[player1-1]
    
    row, col = node
    length = len(board)
    width  = len(board[1])
    
    #Checking if you can move one to the right
    if (col + 2 < width ):
        next_node = board[row][col+2]
        if next_node == 0 and valid_space(player1, opponent, (row, col+2)):
            moves.append((row, col+2))
    #Checking if you can move one to the left
    if (col - 2 >= 0):
        next_node = board[row][col-2]
        if next_node == 0 and valid_space(player1, opponent, (row, col-2)):
            moves.append((row, col-2))
    #Checking if you can move up left
    if (row - 1 >= 0 and col - 1 >= 0):
        next_node = board[row-1][col-1]
        if next_node == 0 and valid_space(player1, opponent, (row-1, col-1)):
            moves.append((row-1, col-1))
    #Checking if you can move up right
    if (row - 1 >= 0 and col + 1 < width ):
        next_node = board[row-1][col+1]
        if next_node == 0 and valid_space(player1, opponent, (row-1, col+1)):
            moves.append((row-1, col+1))
    #Checking if you can move down left
    if (row + 1 < length and col - 1  >= 0):
        next_node = board[row+1][col-1]
        if next_node == 0 and valid_space(player1, opponent, (row+1, col-1)):
            moves.append((row+1, col-1))
    #Checking if you can move down right
    if (row + 1 < length and col + 1 < width):
        next_node = board[row+1][col+1]
        if next_node == 0 and valid_space(player1, opponent, (row+1, col+1)):
            moves.append((row+1, col+1))
        
    #Checking for jumps
    #Adds each possible move on a link of jumps
    check_jumps(board, node, player1, moves, opponent, length, width)
    
    return moves
    