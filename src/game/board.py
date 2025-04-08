import pygame
from .constants import *
from ..helpers import logic

class PyGame_Board:
    def __init__(self):
        self.grid = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def draw(self, screen):
        # Gridlines
        pygame.draw.rect(screen, GRID_COLOUR, (MARGIN, MARGIN_TOP, (BOARD_SIZE * CELL_SIZE), (BOARD_SIZE * CELL_SIZE)))
        

        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                rect = pygame.Rect(MARGIN + x * CELL_SIZE, MARGIN_TOP + y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
                pygame.draw.rect(screen, GRID_COLOUR, rect, 1)
                pygame.draw.rect(screen, COLOUR_MAP[self.grid[y][x]], rect)

        #Draw the border around the board
        pygame.draw.rect(screen, BORDER_COLOUR, (MARGIN, MARGIN_TOP, (BOARD_SIZE * CELL_SIZE), (BOARD_SIZE * CELL_SIZE)), BORDER_THICKNESS)

    def place(self, piece, grid_pos, colour):
        for dx, dy in piece.get_shape_offsets():
            x = grid_pos[0] + dx
            y = grid_pos[1] + dy
            self.grid[y][x] = colour
