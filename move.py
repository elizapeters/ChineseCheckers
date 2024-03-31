# move from one spot to another
def move(board, start_row, start_col, end_row, end_col):
    marble_num = board[start_row][start_col]
    board[end_row][end_col] = marble_num
    board[start_row][start_col] = 0
    return
