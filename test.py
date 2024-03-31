from valid_moves import *
from game_initialization import *
from game_over import *

(17,25)

def test_valid_moves():

    board = boardBuilder()

    player1 = 6
    player2 = 1

    moves = valid_moves(board, (3, 9), 6, 1)
    moves = valid_moves(board, (2, 10), 6, 1)
    print(moves)

def test_player_wins():

    board = boardBuilder()

    player1 = 6
    player2 = 1

    for i in range(17):
        for j in range(25):
            if board[i][j] == player1:
                board[i][j] = 0
                if i > 10: 
                    board[i-11][j] = player1

    game_is_over, result = game_over(board, player1, player2)

    if game_is_over:
        print(result)
    else:
        print("Game is still ongoing.")


def test_no_valid_moves():
    board = boardBuilder()

    player1 = 6
    player2 = 1

    moves = valid_moves(board, (3, 9), 6, 1)
    moves = valid_moves(board, (2, 10), 6, 1)
    print(moves)

    game_is_over, result = game_over(board, player1, player2)

    if game_is_over:
        print(result)
    else:
        print("Game is still ongoing.")


#test_valid_moves()
test_player_wins()
#test_no_valid_moves()

# move player 1 to opposite side and make sure player 2 is not oocupying that space