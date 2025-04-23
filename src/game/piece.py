import pygame
from ..gui.constants import *
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
    "I1": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 1),
    "I2": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 3),
    "I3": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 5),
    "I4": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 7),
    "I5": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 9),
    "V3": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 11),
    "O4": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 14),
    "Z4": (BOARD_SIZE * CELL_SIZE + MARGIN*2, MARGIN_TOP + CELL_SIZE * 17),
    "T4": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 5, MARGIN_TOP + CELL_SIZE * 1),
    "L4": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 5, MARGIN_TOP + CELL_SIZE * 4),
    "U": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 7, MARGIN_TOP + CELL_SIZE * 8),
    "P": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 3, MARGIN_TOP + CELL_SIZE * 11),
    "L5": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 3, MARGIN_TOP + CELL_SIZE * 14),
    "N": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 4, MARGIN_TOP + CELL_SIZE * 17),
    "Y": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 10, MARGIN_TOP + CELL_SIZE * 1),
    "X": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 10, MARGIN_TOP + CELL_SIZE * 4),
    "W": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 12, MARGIN_TOP + CELL_SIZE * 8),
    "F": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 8, MARGIN_TOP + CELL_SIZE * 12),
    "Z5": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 8, MARGIN_TOP + CELL_SIZE * 16),
    "T": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 12, MARGIN_TOP + CELL_SIZE * 12),
    "V5": (BOARD_SIZE * CELL_SIZE + MARGIN*2 + CELL_SIZE * 12,  MARGIN_TOP + CELL_SIZE * 16),
}