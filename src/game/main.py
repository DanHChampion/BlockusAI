import pygame
from .blokus import Blokus
from ..gui.constants import *

def main():
    pygame.init()
    ICON = pygame.image.load("./src/gui/icon.png")
    pygame.display.set_icon(ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE)
    pygame.display.set_caption("Blokus")
    clock = pygame.time.Clock()
    game = Blokus(screen, clock)

    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)
        running = game.handle_events()
        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
