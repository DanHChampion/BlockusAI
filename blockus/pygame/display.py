import pygame
import sys

# Colours
RED = (202, 52, 56)
GREEN = (32, 187, 123)
YELLOW = (227, 228, 57)
BLUE = (51, 115, 197)

CELL_SIZE = 20

def display(manager):
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH = HEIGHT = len(manager.board)*CELL_SIZE

    # Colors
    WHITE = (255, 255, 255)

    # Create the Pygame screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blockus")

    # Main loop
    running = True
    game = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        # Clear the screen
        screen.fill(WHITE)
        if game:
            flag = False
            manager.round += 1
            manager.output_text(f"Round: {manager.round}")
            for player in manager.player_list:
                if manager.player_turn(player):
                    flag = True
                # Draw the Game Board
                grid = manager.logic.board
                render_board(screen, grid)

            if not flag:
                manager.end_game()
                game = False

        render_board(screen, grid)

    # Quit Pygame
    pygame.quit()
    sys.exit()

def render_board(screen, data):
    board_size = len(data)
    for row in range(board_size):
        for col in range(board_size):
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if data[row][col] == 1:
                pygame.draw.rect(screen, RED, rect)
            if data[row][col] == 2:
                pygame.draw.rect(screen, GREEN, rect)
            if data[row][col] == 3:
                pygame.draw.rect(screen, YELLOW, rect)
            if data[row][col] == 4:
                pygame.draw.rect(screen, BLUE, rect)
    
    # Update the display
    pygame.display.flip()