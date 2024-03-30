#Checks moves with jumps
def check_jumps(board, node, player1, player2, moves):
    x = node[0]
    y = node[1]
    
     #If spot to the right is occupied and the spot after is empty
    if (board[x+2][y] == player1 or board[x+2][y] == player2) and  (board[x+4][y] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x+4, y))
        check_jumps(jumpboard, (x+4, y), player1, player2, moves)
    #If spot to the left is occupied and the spot after is empty
    if (board[x-2][y] == player1 or board[x-2][y] == player2) and  (board[x-4][y] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x-4, y))
        check_jumps(jumpboard, (x-4, y), player1, player2, moves)
    #If spot to the top left is occupied and the spot after is empty
    if (board[x-1][y+1] == player1 or board[x-1][y+1] == player2) and  (board[x-2][y+2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x-2, y+2))
        check_jumps(jumpboard, (x-2, y+2), player1, player2, moves)
    #If spot to the top right is occupied and the spot after is empty
    if (board[x+1][y+1] == player1 or board[x+1][y+1] == player2) and  (board[x+2][y+2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x+2, y+2))
        check_jumps(jumpboard, (x+2, y+2), player1, player2, moves)
    #If spot to the bottom left is occupied and the spot after is empty
    if (board[x-1][y-1] == player1 or board[x-1][y-1] == player2) and  (board[x-2][y-2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x-2, y-2))
        check_jumps(jumpboard, (x-2, y-2), player1, player2, moves)
    #If spot to the bottom right is occupied and the spot after is empty
    if (board[x+1][y-1] == player1 or board[x+1][y-1] == player2) and  (board[x+2][y-2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x+2, y-2))
        check_jumps(jumpboard, (x+2, y-2), player1, player2, moves)

#Determines the valid moves from the given node
#Board - the board
#node - the place you want to move from
#player1 - number of player making the move
#player2 - number of other player in the game
def valid_moves(board, node, player1, player2):
    #moves is a array of tuples representing locations on the board you can move to
    moves = []
    
    x = node[0]
    y = node[1]
    
    #Checking if you can move one to the right
    if board[x+2][y] == 0:
        moves.append((x+2, y))
    #Checking if you can move one to the left
    if board[x-2][y] == 0:
        moves.append((x-2, y))
    #Checking if you can move up left
    if board[x-1][y+1] == 0:
        moves.append((x-1, y+1))
    #Checking if you can move up right
    if board[x+1][y+1] == 0:
        moves.append((x+1, y+1))
    #Checking if you can move down left
    if board[x+1][y-1] == 0:
        moves.append((x+1, y-1))
    #Checking if you can move down right
    if board[x+1][y-2] == 0:
        moves.append((x-1, y-1))
        
    #Checking for jumps
    #Adds each possible move on a link of jumps
    
    #If spot to the right is occupied and the spot after is empty
    if (board[x+2][y] == player1 or board[x+2][y] == player2) and  (board[x+4][y] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x+4, y))
        check_jumps(jumpboard, (x+4, y), player1, player2, moves)
    #If spot to the left is occupied and the spot after is empty
    if (board[x-2][y] == player1 or board[x-2][y] == player2) and  (board[x-4][y] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x-4, y))
        check_jumps(jumpboard, (x-4, y), player1, player2, moves)
    #If spot to the top left is occupied and the spot after is empty
    if (board[x-1][y+1] == player1 or board[x-1][y+1] == player2) and  (board[x-2][y+2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x-2, y+2))
        check_jumps(jumpboard, (x-2, y+2), player1, player2, moves)
    #If spot to the top right is occupied and the spot after is empty
    if (board[x+1][y+1] == player1 or board[x+1][y+1] == player2) and  (board[x+2][y+2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x+2, y+2))
        check_jumps(jumpboard, (x+2, y+2), player1, player2, moves)
    #If spot to the bottom left is occupied and the spot after is empty
    if (board[x-1][y-1] == player1 or board[x-1][y-1] == player2) and  (board[x-2][y-2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x-2, y-2))
        check_jumps(jumpboard, (x-2, y-2), player1, player2, moves)
    #If spot to the bottom right is occupied and the spot after is empty
    if (board[x+1][y-1] == player1 or board[x+1][y-1] == player2) and  (board[x+2][y-2] == 0):
        jumpboard = board.copy()
        #This is so in the recursion there isn't an infinte loop of jumping back and forth
        jumpboard[x][y] = -1
        moves.append((x+2, y-2))
        check_jumps(jumpboard, (x+2, y-2), player1, player2, moves)
      
    return moves