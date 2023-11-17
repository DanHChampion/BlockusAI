import pygame
import sys
import time

from . import render

WHITE = (255, 255, 255)

CELL_SIZE = 20

def run(manager):
    # Initialize Pygame
    pygame.init()

    # Constants
    BOARD_SIZE = len(manager.board)
    WIDTH = BOARD_SIZE*CELL_SIZE + 500
    HEIGHT = BOARD_SIZE*CELL_SIZE + 580
    CENTER = [WIDTH//2, HEIGHT//2] # cols, rows
    FONT = pygame.font.Font("./blockus/pygame/VarelaRound-Regular.ttf", 18)
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
    count = 0
    end_game_check = 0
    round = manager.round
    timer = time.time()

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

        if flag:
            manager.round = count // NO_OF_PLAYERS + 1
            if round != manager.round:
                round = manager.round
                print(f"Round: {round}")
                end_game_check = 0
            player = PLAYERS[count % NO_OF_PLAYERS]
            if manager.player_turn(player):
                end_game_check = 0
            else:
                end_game_check += 1
            
            if end_game_check == 4:
                flag = False
                timer = format(time.time()-timer,".2f")
                print(f"Game finished after {timer}s") # Print how long game took
                manager.end_game()
            count +=1



        render.render_players(SCREEN, PLAYERS, CENTER, len(grid), FONT)
        render.render_board(SCREEN, grid, CENTER)
        clock.tick(60)


    # Quit Pygame
    pygame.quit()
    sys.exit()


# timer = time.time()
# while(flag):
#     manager.round += 1
#     manager.output_text(f"Round: {manager.round}")
#     flag = False
#     for player in manager.player_list:
#         if manager.player_turn(player):
#             flag = True

#     if manager.round == MAX_ROUNDS: break
# timer = format(time.time()-timer,".2f")
# print(f"Game finished after {timer}s") # Print how long game took
# manager.end_game()