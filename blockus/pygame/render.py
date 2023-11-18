import pygame
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../configurations/.env')
load_dotenv(dotenv_path=dotenv_path)

# Colours
RED = (202, 52, 56)
GREEN = (32, 187, 123)
YELLOW = (227, 228, 57)
BLUE = (51, 115, 197)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (180, 180, 180)

COLOUR_MAP = {1: RED, 2: GREEN, 3: YELLOW, 4: BLUE}

CELL_SIZE = int(os.environ.get('CELL_SIZE'))

def render_board(screen, data, center):
    border_thickness = CELL_SIZE//5
    board_size = len(data)
    middle = (board_size*CELL_SIZE)//2
    offset = [center[0] - middle, center[1] - middle]

    # Border
    for i in range(4):
        pygame.draw.rect(
            screen, 
            BLACK,
            (-border_thickness + offset[0],
            -border_thickness + offset[1],
            (board_size*CELL_SIZE)+(border_thickness*2)-1,
            (board_size*CELL_SIZE)+(border_thickness*2)-1),
            border_thickness
        )

    for row in range(board_size):
        for col in range(board_size):
            rect = (col * CELL_SIZE + offset[0], row * CELL_SIZE + offset[1], CELL_SIZE-1, CELL_SIZE-1)
            cell_value = data[row][col]
            if cell_value in COLOUR_MAP:
                pygame.draw.rect(screen, COLOUR_MAP[cell_value], rect)


def render_players(screen, data, center, board_size, font, current = 0):
    width = CELL_SIZE*8
    height = CELL_SIZE*2
    padding = CELL_SIZE
    border_thickness = CELL_SIZE//5
    middle = [width//2, height//2]
    half_board_size = (board_size*CELL_SIZE)//2
    translate_x = half_board_size + width//2 + padding
    translate_y = half_board_size - height//2
    
    for player in data:
        if player.colour == 1:
            offset = [center[0] - middle[0] - translate_x, center[1] - middle[1] - translate_y]
            colour = RED
        if player.colour == 2:
            offset = [center[0] - middle[0] - translate_x, center[1] - middle[1] + translate_y]
            if board_size == 14:
                offset = [center[0] - middle[0] + translate_x, center[1] - middle[1] + translate_y]
            colour = GREEN
        if player.colour == 3:
            offset = [center[0] - middle[0] + translate_x, center[1] - middle[1] + translate_y]
            colour = YELLOW
        if player.colour == 4:
            offset = [center[0] - middle[0] + translate_x, center[1] - middle[1] - translate_y]
            colour = BLUE
        
        text = font.render(player.name, True, colour)
        textRect = text.get_rect()
        textRect.center = (offset[0] + middle[0], offset[1] + middle[1])
        screen.blit(text, textRect)

        border_colour = BLACK
        if current == player.colour:
            border_colour = GREY
        # Border
        for i in range(4):
            pygame.draw.rect(
                screen, 
                border_colour,
                (-border_thickness + offset[0],
                -border_thickness + offset[1],
                width+(border_thickness*2),
                height+(border_thickness*2)),
                border_thickness
            )
