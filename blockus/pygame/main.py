import pygame
import sys
import time
import os
from dotenv import load_dotenv
from pathlib import Path

from . import render

dotenv_path = Path('../configurations/.env')
load_dotenv(dotenv_path=dotenv_path)

WHITE = (255, 255, 255)

CELL_SIZE = int(os.environ.get('CELL_SIZE'))
FPS = int(os.environ.get('FPS'))

def run(manager):
    # Initialize Pygame
    pygame.init()

    # Constants
    BOARD_SIZE = len(manager.board)
    WIDTH = BOARD_SIZE*CELL_SIZE + CELL_SIZE*20
    HEIGHT = BOARD_SIZE*CELL_SIZE + CELL_SIZE*3
    CENTER = [WIDTH//2, HEIGHT//2] # cols, rows
    FONT = pygame.font.Font("./blockus/pygame/VarelaRound-Regular.ttf", CELL_SIZE-1)
    PLAYERS = manager.player_list
    NO_OF_PLAYERS = len(PLAYERS)

    # Create the Pygame screen
    ICON = pygame.image.load("./blockus/pygame/icon.png")
    pygame.display.set_icon(ICON)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blockus")

    # Clear the screen
    SCREEN.fill(WHITE)

    # Main loop
    running = True
    clock = pygame.time.Clock()

    # Initialise
    print(f"Starting Game with {NO_OF_PLAYERS} players...")
    flag = True
    end_game_check = 0
    round = manager.round
    timer = time.time()

    # Human Player States
    wait_for_human = False
    human_has_legal_moves = False


    # Game Loop
    print("Playing...")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        grid = manager.board
        SCREEN.fill(WHITE)

        if flag:
            manager.round = manager.turn // NO_OF_PLAYERS + 1
            if round != manager.round:
                round = manager.round
                print(f"Round: {round}")
                end_game_check = 0
            player = PLAYERS[manager.turn % NO_OF_PLAYERS]
            end_game_check += 1

            if player.ai.version == "hu":
                wait_for_human = True
                if not human_has_legal_moves:
                    human_has_legal_moves = manager.player_turn(player)
                    if human_has_legal_moves:
                        print("Waiting for move...")
                end_game_check = 0
            elif manager.player_turn(player):
                end_game_check = 0

            if end_game_check == NO_OF_PLAYERS:
                flag = False
                timer = format(time.time()-timer,".2f")
                print(f"Game finished after {timer}s") # Print how long game took
                manager.end_game()
            



        render.render_players(SCREEN, PLAYERS, CENTER, len(grid), FONT)
        render.render_board(SCREEN, grid, CENTER)
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)


    # Quit Pygame
    pygame.quit()
    sys.exit()