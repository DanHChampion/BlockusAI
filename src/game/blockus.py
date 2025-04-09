import pygame
import os
from .piece import PyGame_Piece
from .constants import *
from .manager import PyGame_Manager
from ..helpers.logic import find_legal_corners, is_move_legal, place_piece

class Blockus:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.manager = PyGame_Manager()
        self.selected = None
        self.pieces = self.manager.player_list[self.manager.hm_player_index].remaining_pieces

        self.clock = clock
        
        font_path = os.path.join(os.path.dirname(__file__), "./font/Micro5-Regular.ttf")
        self.font = pygame.font.Font(font_path, round(CELL_SIZE * 1.2))  # Normal font

        self.restart_rect = pygame.Rect(SCREEN_WIDTH - (4 * CELL_SIZE) - MARGIN, MARGIN, (4 * CELL_SIZE), (1.3 * CELL_SIZE))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.handle_event(event)
        return True

    def handle_event(self, event):
        # Check if turn is humans turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart_rect.collidepoint(event.pos):
                    self.manager.intialise()
                    self.pieces = self.manager.player_list[self.manager.hm_player_index].remaining_pieces
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
                        self.draw()
                        self.manager.player_turn()
                    self.selected = None

            elif event.type == pygame.KEYDOWN:
                if self.selected:
                    if event.key == pygame.K_r:
                        self.selected.rotate()
                    elif event.key == pygame.K_f:
                        self.selected.flip()

    def update(self):
        # Selected piece is being dragged
        if self.selected:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.selected.move_to((mouse_x, mouse_y))
        else:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            hovering = False

            # Hovering over a piece
            for piece in self.pieces:
                if any(pygame.Rect(piece.position[0] + dx * CELL_SIZE, piece.position[1] + dy * CELL_SIZE,
                                CELL_SIZE, CELL_SIZE).collidepoint((mouse_x, mouse_y)) for dx, dy in piece.get_shape_offsets()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    hovering = True
                    break

            # Hovering over the restart button
            if self.restart_rect.collidepoint((mouse_x, mouse_y)):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                hovering = True

            if not hovering:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self):
        # Draw board
        self.manager.board.draw(self.screen)

        # Draw all pieces
        for piece in self.pieces:
            piece.draw(self.screen)

        # Draw pause button
        pygame.draw.rect(self.screen, GRID_COLOUR, self.restart_rect)
        pygame.draw.rect(self.screen, BORDER_COLOUR, self.restart_rect, BORDER_THICKNESS)
        pause_text = self.font.render("Restart", True, BLACK)
        self.screen.blit(pause_text, (self.restart_rect.x + CELL_SIZE // 2, self.restart_rect.y))

        # Draw FPS counter
        fps_rect = pygame.Rect(SCREEN_WIDTH - (4 * CELL_SIZE) - MARGIN, MARGIN + (1.7 * CELL_SIZE), (4 * CELL_SIZE), (1.3 * CELL_SIZE))
        pygame.draw.rect(self.screen, GRID_COLOUR, fps_rect)
        pygame.draw.rect(self.screen, BORDER_COLOUR, fps_rect, BORDER_THICKNESS)
        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, BLACK)
        self.screen.blit(fps_text, (fps_rect.x + CELL_SIZE // 2, fps_rect.y))

        # Draw player rectangles and names
        player_rects = [
            pygame.Rect(MARGIN, MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE)),
            pygame.Rect(MARGIN + (8 * CELL_SIZE), MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE)),
            pygame.Rect(MARGIN + (16 * CELL_SIZE), MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE)),
            pygame.Rect(MARGIN + (24 * CELL_SIZE), MARGIN, (7 * CELL_SIZE), (3 * CELL_SIZE))
        ]

        for i, rect in enumerate(player_rects):
            player = self.manager.player_list[i]
            pygame.draw.rect(self.screen, COLOUR_MAP[player.colour], rect)
            pygame.draw.rect(self.screen, BORDER_COLOUR, rect, BORDER_THICKNESS)

            # Draw player details
            name_text = self.font.render(player.name, True, BLACK)
            ai_text = self.font.render(player.ai_version, True, BLACK)
            score_text = self.font.render(str(player.current_score()), True, BLACK)

            self.screen.blit(name_text, (rect.x + CELL_SIZE, rect.y + CELL_SIZE * 0.4))
            self.screen.blit(ai_text, (rect.x + CELL_SIZE, rect.y + CELL_SIZE * 1.4))
            self.screen.blit(score_text, (rect.x + CELL_SIZE * 5, rect.y + CELL_SIZE * 0.8))
        
