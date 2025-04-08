import pygame
from .piece import PyGame_Piece
from .ui import UI
from .constants import *
from .manager import PyGame_Manager

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.manager = PyGame_Manager(4)
        self.ui = UI(self.screen, self.manager, self.clock)
        self.selected_piece = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.ui.handle_event(event)
        return True

    def update(self):
        self.ui.update()

    def draw(self):
        self.ui.draw(self.screen)
