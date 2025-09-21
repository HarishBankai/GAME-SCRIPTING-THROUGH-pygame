# Import the Pygame library
import pygame
# Import useful constants like QUIT, MOUSEBUTTONDOWN
from pygame.locals import *

# --- Constants (game settings) ---
WIDTH = 320                       # Width of the window
HEIGHT = 480                      # Height of the window
CELL_SIZE = 80                    # Size of each square cell in the 3x3 grid
LINE_COLOR = (255, 255, 255)      # White color for grid lines
CIRCLE_COLOR = (0, 0, 255)        # Blue color for circle (Player 2)
CROSS_COLOR = (255, 0, 0)         # Red color for cross (Player 1)
X_MARGIN = 40                     # Left margin for centering the board
Y_MARGIN = 100                    # Top margin for centering the board

# --- Setup Pygame ---
pygame.init()                     # Initialize all imported Pygame modules
screen = pygame.display.set_mode((WIDTH, HEIGHT))   # Create a window with given width and height
pygame.display.set_caption("Tic Tac Toe")           # Set the title of the game window

# --- Game variables ---
board = [[0 for _ in range(3)] for _ in range(3)]   # 3x3 grid initialized with 0 (empty cells)
current_player = 1               # Player 1 starts the game
game_over = False                # Game is running until someone wins or it's a draw

# --- Functions ---
def draw():
    screen.fill((0, 0, 0))        # Fill the screen with black background
    
    # Draw the grid lines
    for i in range(1, 3):         # Draw 2 vertical and 2 horizontal lines (since it's 3x3)
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR,
                         (X_MARGIN + i * CELL_SIZE, Y_MARGIN),           # Start point
                         (X_MARGIN + i * CELL_SIZE, Y_MARGIN + 3 * CELL_SIZE), 3)  # End point and thickness
        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR,
                         (X_MARGIN, Y_MARGIN + i * CELL_SIZE),           # Start point
                         (X_MARGIN + 3 * CELL_SIZE, Y_MARGIN + i * CELL_SIZE), 3)  # End point and thickness

    # Draw symbols (crosses and circles) inside the cells
    for row in range(3):          # Loop through all rows
        for col in range(3):      # Loop through all columns
            x = X_MARGIN + col * CELL_SIZE   # Top-left X position of the current cell
            y = Y_MARGIN + row * CELL_SIZE   # Top-left Y position of the current cell

            if board[row][col] == 1:  # If Player 1 has marked this cell (cross)
                # Draw an "X" with two diagonal lines
                pygame.draw.line(screen, CROSS_COLOR, (x + 10, y + 10), 
                                 (x + CELL_SIZE - 10, y + CELL_SIZE - 10), 4)
                pygame.draw.line(screen, CROSS_COLOR, (x + CELL_SIZE - 10, y + 10), 
                                 (x + 10, y + CELL_SIZE - 10), 4)
            elif board[row][col] == 2:  # If Player 2 has marked this cell (circle)
                # Draw a circle centered in the cell
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 10, 4)

    pygame.display.flip()         # Update the full display with all drawings

def check_winner():
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:  # Same row filled
            return board[i][0]   # Return the winning player
        if board[0][i] == board[1][i] == board[2][i] != 0:  # Same column filled
            return board[0][i]

    # Check the two diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:      # Top-left to bottom-right
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:      # Top-right to bottom-left
        return board[0][2]

    # Check for draw (if all cells are filled and no winner)
    if all(cell != 0 for row in board for cell in row):     # Flattened check
        return -1  # Return -1 to indicate draw

    return 0  # No winner yet, game continues

# --- Main loop ---
draw()                        # Draw the initial empty grid
while not game_over:          # Keep running until game_over becomes True
    for event in pygame.event.get():     # Handle all incoming events
        if event.type == QUIT:           # If player clicks the close button
            game_over = True             # End the loop and exit

        elif event.type == MOUSEBUTTONDOWN and not game_over:  # Handle mouse click
            x, y = pygame.mouse.get_pos()   # Get click coordinates
            row = (y - Y_MARGIN) // CELL_SIZE   # Convert Y coordinate into board row
            col = (x - X_MARGIN) // CELL_SIZE   # Convert X coordinate into board column

            # Ensure the click is inside the 3x3 grid
            if 0 <= row < 3 and 0 <= col < 3:
                # If the cell is empty, make a move
                if board[row][col] == 0:
                    board[row][col] = current_player   # Place current player's symbol
                    draw()                             # Redraw the board with new move

                    winner = check_winner()            # Check if anyone has won
                    if winner != 0:                    # If winner is found or it's a draw
                        game_over = True               # Stop the game
                        if winner == -1:               # Draw case
                            print("It's a draw!")
                        else:                          # Someone won
                            print(f"Player {winner} wins!")
                    else:
                        current_player = 3 - current_player  # Switch player (1 -> 2, 2 -> 1)