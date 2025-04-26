# Chinese Checkers

A Python implementation of the Chinese Checkers board game with AI opponents

## Features

- Interactive GUI built with Pygame
- Support for 2-6 players
- AI opponent using Minimax algorithm
- Valid move checking and game state management
- Win condition detection

## Requirements

- Python 3.x
- Pygame
- NumPy

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
```

2. Install the required dependencies:
```bash
pip install pygame numpy
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Game Rules:
- Each player starts with 10 marbles in their home triangle
- Players take turns moving their marbles
- A marble can move to an adjacent empty space or jump over other marbles
- The goal is to move all your marbles to the opposite triangle
- The first player to move all their marbles to the opposite triangle wins

## Project Structure

- `main.py` - Main game entry point
- `gui.py` - Graphical user interface implementation
- `game_initialization.py` - Board setup and initialization
- `valid_moves.py` - Move validation logic
- `game_over.py` - Win condition checking
- `minimax.py` - AI opponent implementation
- `move.py` - Move representation
- `test.py` - Test cases
