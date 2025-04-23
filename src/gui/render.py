import pygame
import os

from ..configurations.config import configuration
from .constants import *



CELL_SIZE = configuration.CELL_SIZE

def render_board(screen, data, center):
    middle = (BOARD_SIZE*CELL_SIZE)//2
    offset = [center[0] - middle, center[1] - middle]
    
    # Gridlines
    pygame.draw.rect(screen, GREY, (offset[0],  offset[1], (BOARD_SIZE*CELL_SIZE), (BOARD_SIZE*CELL_SIZE)))

    # Border
    pygame.draw.rect(
        screen, 
        BLACK,
        (-BORDER_THICKNESS + offset[0],
        -BORDER_THICKNESS + offset[1],
        (BOARD_SIZE*CELL_SIZE)+(BORDER_THICKNESS*2)-1,
        (BOARD_SIZE*CELL_SIZE)+(BORDER_THICKNESS*2)-1),
        BORDER_THICKNESS
    )

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = (col * CELL_SIZE + offset[0], row * CELL_SIZE + offset[1], CELL_SIZE-1, CELL_SIZE-1)
            cell_value = data[row][col]
            if cell_value in COLOUR_MAP:
                pygame.draw.rect(screen, COLOUR_MAP[cell_value], rect)

