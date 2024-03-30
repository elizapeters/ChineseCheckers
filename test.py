from valid_moves import *
from game_initialization import *

(17,25)

board = boardBuilder()

moves = valid_moves(board, (3, 9), 6, 1)
moves = valid_moves(board, (2, 10), 6, 1)
print(moves)