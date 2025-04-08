import pygame
import os
from .constants import *
from ..configurations import config
from .piece import PyGame_Piece
import json
from ..helpers import logic
from ..helpers.logic import find_legal_corners, is_move_legal, place_piece


class UI:
    def __init__(self, screen, manager, clock):
        self.screen = screen
        self.selected = None
        self.manager = manager
        self.pieces = self.manager.player_list[0].remaining_pieces

        self.clock = clock
        
        font_path = os.path.join(os.path.dirname(__file__), "./font/Micro5-Regular.ttf")
        self.font = pygame.font.Font(font_path, 24) # Normal font
        self.st_font = pygame.font.Font(font_path, 24)
        self.st_font.set_strikethrough(True) # Strikethrough font for player names

        self.restart_rect = pygame.Rect(SCREEN_WIDTH - (4 * CELL_SIZE) - MARGIN, MARGIN, (4 * CELL_SIZE), (1.3 * CELL_SIZE))

    def handle_event(self, event):
        # check if turn is humans turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart_rect.collidepoint(event.pos):
                    self.manager.intialise(self.manager.no_of_players)
                    self.pieces = self.manager.player_list[0].remaining_pieces
        if self.manager.current_player.ai_version == "hm":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for piece in self.pieces:
                    if any(pygame.Rect(piece.position[0] + dx * CELL_SIZE, piece.position[1] + dy * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE).collidepoint(event.pos) for dx, dy in piece.get_shape_offsets()):
                        self.selected = piece
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.selected:
                    grid_pos = list(reversed(self.selected.get_grid_position()))
                    legal_corners = [[0, 0]]
                    if self.manager.board.grid[0][0] != 0:
                        legal_corners = find_legal_corners(self.manager.board.grid, self.selected.colour)
                    move = [self.selected.piece, grid_pos, self.selected.piece]
                    if is_move_legal(self.manager.board.grid, move, self.selected.colour, legal_corners):
                        self.manager.board.grid = place_piece(self.manager.board.grid, self.selected.colour, move)
                        self.pieces.remove(self.selected)
                        self.screen.fill(BACKGROUND_COLOUR)
                        self.draw(self.screen)
                        self.manager.player_turn()
                    self.selected = None

            elif event.type == pygame.KEYDOWN:
                if self.selected:
                    if event.key == pygame.K_r:
                        self.selected.rotate()
                    elif event.key == pygame.K_f:
                        self.selected.flip()

    def update(self):
        if self.selected:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.selected.move_to((mouse_x, mouse_y))
        else:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            hovering = False

            # Check if hovering over a piece
            for piece in self.pieces:
                if any(pygame.Rect(piece.position[0] + dx * CELL_SIZE, piece.position[1] + dy * CELL_SIZE,
                                CELL_SIZE, CELL_SIZE).collidepoint((mouse_x, mouse_y)) for dx, dy in piece.get_shape_offsets()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    hovering = True
                    break

            # Check if hovering over buttons (Pause or FPS)
            fps_rect = pygame.Rect(SCREEN_WIDTH - (4 * CELL_SIZE) - MARGIN, MARGIN + (2.5 * CELL_SIZE), (4 * CELL_SIZE), (1.5 * CELL_SIZE))
            if self.restart_rect.collidepoint((mouse_x, mouse_y)) or fps_rect.collidepoint((mouse_x, mouse_y)):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                hovering = True

            # Reset cursor if not hovering over anything
            if not hovering:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen):
        # Draw Board
        self.manager.board.draw(screen)

        # Draw All Pieces
        for piece in self.pieces:
            piece.draw(screen)

    def draw_ui(self,screen):
        # Draw pause button
        pygame.draw.rect(screen, GRID_COLOUR, self.restart_rect)
        pygame.draw.rect(screen, BORDER_COLOUR, self.restart_rect, BORDER_THICKNESS)
        pause_text = self.font.render("Restart", True, BLACK)
        screen.blit(pause_text, (self.restart_rect.x + CELL_SIZE // 2, self.restart_rect.y))

        # Draw FPS counter
        fps_rect = pygame.Rect(SCREEN_WIDTH - (4 * CELL_SIZE) - MARGIN, MARGIN + (1.7 * CELL_SIZE), (4 * CELL_SIZE), (1.3 * CELL_SIZE))
        pygame.draw.rect(screen, GRID_COLOUR, fps_rect)
        pygame.draw.rect(screen, BORDER_COLOUR, fps_rect, BORDER_THICKNESS)
        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, BLACK)
        screen.blit(fps_text, (fps_rect.x + CELL_SIZE // 2, fps_rect.y))

        # Define player rectangles based on the number of players
        player_rects = []
        if self.manager.no_of_players == 2:
            player_rects = [
                pygame.Rect(MARGIN, MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE)),
                pygame.Rect(MARGIN + (8 * CELL_SIZE), MARGIN, (5 * CELL_SIZE), (3 * CELL_SIZE))
            ]
        elif self.manager.no_of_players == 4:
            player_rects = [
                pygame.Rect(MARGIN, MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE)),
                pygame.Rect(MARGIN + (8 * CELL_SIZE), MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE)),
                pygame.Rect(MARGIN + (16 * CELL_SIZE), MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE)),
                pygame.Rect(MARGIN + (24 * CELL_SIZE), MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE))
            ]
        else:
            raise ValueError("Unsupported number of players. Only 2 or 4 players are supported.")

        # Draw player rectangles and names
        for i, rect in enumerate(player_rects):
            player = self.manager.player_list[i]
            pygame.draw.rect(screen, COLOUR_MAP[player.colour], rect)

            # Highlight the current player
            border_colour = ORANGE if player == self.manager.current_player else BORDER_COLOUR
            pygame.draw.rect(screen, border_colour, rect, BORDER_THICKNESS)

            # Draw player details
            name_text = self.font.render(player.name, True, BLACK)
            ai_text = self.font.render(player.ai_version, True, BLACK)

            if player.finished:
                name_text = self.st_font.render(player.name, True, BLACK)
                ai_text = self.st_font.render(player.ai_version, True, BLACK)
            screen.blit(name_text, (rect.x + CELL_SIZE, rect.y + CELL_SIZE//2))
            screen.blit(ai_text, (rect.x + CELL_SIZE, rect.y + CELL_SIZE * 1.5))
        
