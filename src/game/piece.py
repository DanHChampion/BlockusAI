import pygame
from .constants import *
from ..helpers import transformations
from ..helpers.piece import Piece

class PyGame_Piece(Piece):
    def __init__(self, type, colour):
        super().__init__(type, colour)
        
        self.position = initial_positions.get(type)
        self.held = False

    def draw(self, screen):
        for dx, dy in self.get_shape_offsets():
            border_rect = pygame.Rect(self.position[0] + dx * CELL_SIZE, self.position[1] + dy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            rect = pygame.Rect(self.position[0] + dx * CELL_SIZE, self.position[1] + dy * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
            pygame.draw.rect(screen, GREY, border_rect, 1)
            pygame.draw.rect(screen, COLOUR_MAP[self.colour], rect)

    def rotate(self):
        self.piece = transformations.rotate_piece_clockwise(self.piece, 1)

    def flip(self):
        self.piece = transformations.flip_piece_vertical(self.piece)

    def move_to(self, pos):
        self.position = pos

    def get_grid_position(self):
        x = (self.position[0] - MARGIN + CELL_SIZE // 2) // CELL_SIZE
        y = (self.position[1] - MARGIN_TOP + CELL_SIZE // 2) // CELL_SIZE
        return (x, y)

    def get_shape_offsets(self):
        # Convert the piece's 2D array representation into (x, y) offsets.
        offsets = []
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell:
                    offsets.append((x, y))
        return offsets

initial_positions = {
    "I1": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 0),
    "I2": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 2),
    "I3": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 4),
    "I4": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 6),
    "I5": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 8),
    "V3": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 10),
    "O4": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 13),
    "Z4": (SCREEN_WIDTH // 4 * 2 + MARGIN, MARGIN_TOP + CELL_SIZE * 16),
    "T4": (SCREEN_WIDTH // 4 * 3 - CELL_SIZE * 5, MARGIN_TOP + CELL_SIZE * 0),
    "L4": (SCREEN_WIDTH // 4 * 3 - CELL_SIZE * 4, MARGIN_TOP + CELL_SIZE * 3),
    "U": (SCREEN_WIDTH // 4 * 3 - CELL_SIZE * 3, MARGIN_TOP + CELL_SIZE * 7),
    "P": (SCREEN_WIDTH // 4 * 3 - CELL_SIZE * 5, MARGIN_TOP + CELL_SIZE * 10),
    "L5": (SCREEN_WIDTH // 4 * 3 - CELL_SIZE * 5, MARGIN_TOP + CELL_SIZE * 13),
    "N": (SCREEN_WIDTH // 4 * 3 - CELL_SIZE * 5, MARGIN_TOP + CELL_SIZE * 16),
    "Y": (SCREEN_WIDTH // 4 * 3 + CELL_SIZE, MARGIN_TOP + CELL_SIZE * 0),
    "X": (SCREEN_WIDTH // 4 * 3 + CELL_SIZE, MARGIN_TOP + CELL_SIZE * 3),
    "W": (SCREEN_WIDTH // 4 * 3 + CELL_SIZE, MARGIN_TOP + CELL_SIZE * 7),
    "F": (SCREEN_WIDTH // 4 * 3, MARGIN_TOP + CELL_SIZE * 11),
    "Z5": (SCREEN_WIDTH // 4 * 3, MARGIN_TOP + CELL_SIZE * 15),
    "T": (SCREEN_WIDTH // 4 * 3 + CELL_SIZE * 4, MARGIN_TOP + CELL_SIZE * 11),
    "V5": (SCREEN_WIDTH // 4 * 3 + CELL_SIZE * 4,  MARGIN_TOP + CELL_SIZE * 15),
}