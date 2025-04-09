import pygame
import os

from ..configurations.config import configuration

# Colours
RED = (202, 52, 56)
GREEN = (32, 187, 123)
YELLOW = (227, 228, 57)
BLUE = (51, 115, 197)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (180, 180, 180)
PURPLE = (128, 0, 128)

COLOUR_MAP = {0: WHITE, 1: RED, 2: GREEN, 3: YELLOW, 4: BLUE}

CELL_SIZE = configuration.CELL_SIZE

def render_board(screen, data, center):
    border_thickness = CELL_SIZE // 8
    board_size = len(data)
    middle = (board_size*CELL_SIZE)//2
    offset = [center[0] - middle, center[1] - middle]
    
    # Gridlines
    pygame.draw.rect(screen, GREY, (offset[0],  offset[1], (board_size*CELL_SIZE), (board_size*CELL_SIZE)))

    # Border
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

