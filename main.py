from gui import gen_gui
from game_initialization import boardBuilder

def main():
    # Initialize the game board
    board = boardBuilder()
    
    # Start the GUI
    gen_gui(board)

if __name__ == "__main__":
    main()
