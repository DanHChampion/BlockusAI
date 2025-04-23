import time
import random
import pygame
from ..gui.constants import *
from ..configurations.constants import BOARD_SIZE, NUM_PLAYERS, ALL_PIECES
from ..helpers import logic
from .piece import PyGame_Piece
from .board import PyGame_Board
from ..helpers.player import Player
from ..helpers import draw


class PyGame_Manager():
    def __init__(self):
        self.intialise()
        self.running = True

    def intialise(self):
        self.round = 0
        self.turn = 0

        self.no_of_players = NUM_PLAYERS
        
        ai_versions = ["hm"] + ["v3" for _ in range(1, self.no_of_players)]
        print("AI versions: ", ai_versions)
        self.ai_versions = ai_versions

        self.player_list = [Player(player, self.ai_versions[player - 1]) for player in range(1, self.no_of_players + 1)]

        # Randomise Order
        shift = random.randint(1, self.no_of_players)
        self.player_list = self.player_list[shift:] + self.player_list[:shift]

        self.board_size = BOARD_SIZE
        self.board = PyGame_Board()

        self.available_pieces_types = ALL_PIECES
        for player in self.player_list:
            player.remaining_pieces = [PyGame_Piece(piece_type, player.colour) for piece_type in self.available_pieces_types]

        # Get position of hm player
        for i, player in enumerate(self.player_list):
            if player.ai_version == "hm":
                self.hm_player_index = i
                break

        self.start_time = time.time()
        self.running = True
        self.current_player = self.player_list[0]
        self.start_game()

    def start_game(self):
        print(f"Starting game with {self.no_of_players} players...")
        self.player_turn()

    def end_game(self):
        runtime = format(time.time() - self.start_time, ".2f")
        print("Game Over")
        print(f"Game finished after {runtime}s")
        print(f"Played a total of {self.round} rounds")

    def player_turn(self):
        pygame.display.update()
        self.current_player = self.player_list[self.turn % self.no_of_players]
        if self.turn % self.no_of_players == 0:
            self.round += 1
        self.turn += 1

        self.player_string = draw.render_cell(self.current_player.colour, str(self.current_player))

        print(f"Round: {self.round} | Turn: {self.turn} | Player: {self.player_string}")

        if all(player.finished for player in self.player_list):
            self.end_game()
            return

        if self.current_player.finished:
            self.player_turn()
            return

        if self.current_player.ai_version == "hm":
            self.handle_human_turn()
        else:
            self.handle_ai_turn()

    def handle_human_turn(self):
        print(f"Human {self.player_string} is playing...")
        available_pieces = self.current_player.remaining_pieces.copy()

        legal_corners = self.get_legal_corners()
        legal_moves = logic.find_legal_moves(self.board.grid, legal_corners, available_pieces, self.current_player.colour)

        if len(legal_moves) == 0 and self.round != 1:
            self.current_player.finished = True
            print(f"{self.player_string} has no legal moves...")
            self.player_turn()

    def handle_ai_turn(self):
        print(f"AI {self.player_string} is thinking...")
        available_pieces = self.current_player.remaining_pieces.copy()

        legal_corners = self.get_legal_corners()
        legal_moves = logic.find_legal_moves(self.board.grid, legal_corners, available_pieces, self.current_player.colour)

        if legal_moves:
            final_move = self.current_player.generate_move(legal_moves, self.board.grid, self.round)

            self.current_player.remaining_pieces.remove(final_move[2])
            self.board.grid = logic.place_piece(self.board.grid, self.current_player.colour, final_move)
        else:
            self.current_player.finished = True
            print(f"{self.player_string} has no legal moves...")

        self.player_turn()

    def get_legal_corners(self):
        if self.round == 1:
            return logic.get_starting_corner(self.board_size, self.current_player.colour)
        return logic.find_legal_corners(self.board.grid, self.current_player.colour)

            
        
