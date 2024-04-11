import pygame
import sys
from valid_moves import *
from game_initialization import *
from game_over import *
from move import *
from minimax import *
from minmaxab import *

def distance(p1, p2):
    """Calculate the distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def get_next_turn(current_turn):
    if (current_turn == 6):
        return 1
    return current_turn+1



def gen_gui(starting_board):
    board = starting_board[0]
    locations = starting_board[1]
    print(locations)
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (236, 252, 2)
    GREEN = (32, 252, 2)
    BLUE = (3, 65, 252)
    PURPLE = (247, 118, 5)
    PINK = (255, 0, 247)

    # Define constants for the game board
    CELL_SIZE = 30
    PADDING = 5
    MARBLE_RADIUS = 20
    OUTLINE_WIDTH = 2

    # Initialize Pygame
    pygame.init()

    # Calculate window size based on the game board size
    WINDOW_SIZE = (CELL_SIZE * len(board[0]) + 2 * PADDING, CELL_SIZE * len(board) + 2 * PADDING)

    # Create the screen
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Chinese Checkers")
    COLORS = {
        -1: BLACK,  # not included in board
        0: WHITE,   # empty
        1: RED,     # Player 1's marble color
        2: PINK,
        3: GREEN,
        4: YELLOW,
        5: PURPLE,
        6: BLUE
    }
    current_player = 6
    first_click = None

    # Main loop
    while True:
        # Handle events
        if (current_player == 7):
            print("PLAYER ", current_player)
            #current_player = get_next_turn(current_player)
            start_end_dict = {}
            all_moves = []
            # do the best move for the ai
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if (board[i][j] == current_player):
                        possible_moves = valid_moves(board, (i,j), current_player)
                        for one_move in possible_moves:
                            all_moves.append(((i,j),one_move))
                        #all_moves = valid_moves(board, (i,j), current_player)
                        #best_move = get_best_move(board, all_moves, (i,j), current_player)
                        # if (best_move is not None):
                        #     starting_tuple = (i,j)
                        #     start_end_dict[starting_tuple] = best_move
                        #     move(board, i, j, best_move[0], best_move[1])
            
            opt_move = best_move(board, all_moves, current_player)
            #opt_move = best_of_best(board,start_end_dict, current_player)
            move(board, opt_move[0][0], opt_move[0][1], opt_move[1][0], opt_move[1][1])
            findAndReplaceMarb(locations, opt_move, current_player)
            if game_over(board):
                print("GAME OVER!!")
                print("Player ", current_player, " Wins!")
                break
            current_player = get_next_turn(current_player)
        if(current_player != 7):
            print("PLAYER ", current_player)
            prev_goal_node = get_goal_node(board, current_player)
            eval, move_to_move = minimax(board.copy(), 2, True, float('-inf'), float('inf'), current_player, copy.deepcopy(locations), prev_goal_node)
            move(board, move_to_move[0][0], move_to_move[0][1], move_to_move[1][0], move_to_move[1][1])
            findAndReplaceMarb(locations, move_to_move, current_player)
            current_player = get_next_turn(current_player)
            if game_over(board):
                print("GAME OVER!!")
                print("Player  ", current_player, " Wins!")
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # Check if any marble circle was clicked
                for i, row in enumerate(board):
                    for j, cell in enumerate(row):
                        if cell != -1:  # Skip slots not in the star shape
                            circle_center = (PADDING + j * CELL_SIZE + CELL_SIZE // 2, PADDING + i * CELL_SIZE + CELL_SIZE // 2)
                            if distance(mouse_pos, circle_center) <= MARBLE_RADIUS:
                                m = board[i][j]
                                if (m == 6 and first_click is None):
                                    first_click = (i,j)
                                elif (first_click is not None and m == 0):
                                    second_click = (i,j)
                                    if (valid_moves(board, first_click, 6).__contains__(second_click)):
                                        print("movin off clicks")
                                        move(board, first_click[0], first_click[1], second_click[0], second_click[1])
                                        if game_over(board):
                                            print("GAME OVER!!")
                                            print("Player ", current_player, " Wins!")
                                            break
                                        
                                        current_player = get_next_turn(current_player)
                                        #current_player = 1
                                    else:
                                        print("Invalid move try again!")
                                    first_click = None
                                else:
                                    first_click = None
                                print("Clicked on circle at:", (i, j))  # Replace this with your desired action

        # Clear the screen
        screen.fill(WHITE)

        # Draw the game board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != -1:  # Skip slots not in the star shape
                    color = COLORS[cell]
                    # Draw filled circle for marble
                    pygame.draw.circle(screen, color, (PADDING + j * CELL_SIZE + CELL_SIZE // 2, PADDING + i * CELL_SIZE + CELL_SIZE // 2), MARBLE_RADIUS)
                    # Draw outline circle
                    pygame.draw.circle(screen, BLACK, (PADDING + j * CELL_SIZE + CELL_SIZE // 2, PADDING + i * CELL_SIZE + CELL_SIZE // 2), MARBLE_RADIUS, OUTLINE_WIDTH)
        
        if (first_click is not None):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if (valid_moves(board, first_click, 6).__contains__((i,j))):  
                        color = (153,204,255)
                        pygame.draw.circle(screen, color, (PADDING + j * CELL_SIZE + CELL_SIZE // 2, PADDING + i * CELL_SIZE + CELL_SIZE // 2), MARBLE_RADIUS)
                        pygame.draw.circle(screen, BLACK, (PADDING + j * CELL_SIZE + CELL_SIZE // 2, PADDING + i * CELL_SIZE + CELL_SIZE // 2), MARBLE_RADIUS, OUTLINE_WIDTH)

        # Update the display
        pygame.display.flip()

board = boardBuilder()
gen_gui(board)
