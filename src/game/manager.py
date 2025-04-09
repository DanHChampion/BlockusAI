import time
import random
import pygame
import os
from .constants import *
from ..configurations.config import configuration
from ..helpers import logic
from .piece import PyGame_Piece
from .board import PyGame_Board
from ..helpers.player import Player
import json

class PyGame_Manager():
    def __init__(self, no_of_players):
        self.intialise(no_of_players)
        self.running = True

    def intialise(self, no_of_players):
        self.round = 0
        self.turn = 0
        
        ai_versions = ["hm"] + ["v4" for _ in range(1, no_of_players)]
        print("AI versions: ", ai_versions)
        self.ai_versions = ai_versions

        self.no_of_players = no_of_players
        self.player_list = [Player(player, self.ai_versions[player - 1]) for player in range(1, no_of_players + 1)]

        # Randomise Order
        shift = random.randint(1, 4)
        self.player_list = self.player_list[shift:] + self.player_list[:shift]

        self.board_size = BOARD_SIZE
        self.board = PyGame_Board()

        self.available_pieces_types = json.loads(configuration.ALL_PIECES)
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
        print(f"Turn: {self.turn} - Player: {self.current_player.name}")
        # Redraw the game window
        pygame.display.update()
        self.current_player = self.player_list[(self.turn % self.no_of_players)]
        print(f"Turn: {self.turn} - Player: {self.current_player.name}")
        if self.turn % self.no_of_players == 0:
            self.round += 1
        self.turn += 1
        print(f"Round: {self.round} Turn: {self.turn} - Player: {self.current_player.name}")
        if all(player.finished for player in self.player_list):
            self.end_game()
            return
        if self.current_player.finished:
            self.player_turn()
            return
        if self.current_player.ai_version == "hm":
            # Human player
            print(f"Human {self.current_player.name} is playing...")
            # check if player has any legal moves
            available_pieces = self.current_player.remaining_pieces.copy()
            if self.round == 1:
                match self.current_player.colour:
                    case 1: # Red starts in top-left
                        legal_corners = [[0,0]]
                    case 2: # Green starts in bottom-left but bottom-right if there are only 2 players
                        if self.no_of_players != 2:
                            legal_corners = [[self.board_size-1,0]]
                        else:
                            legal_corners = [[self.board_size-1,self.board_size-1]]
                    case 3: # Yellow starts in bottom-right
                        legal_corners = [[self.board_size-1,self.board_size-1]]
                    case 4: # Blue starts in top-right
                        legal_corners = [[0,self.board_size-1]]
                    case _:
                        raise ValueError("Invalid Colour")
            else:
                legal_corners = logic.find_legal_corners(self.board.grid, self.current_player.colour)

            print(f"Legal Corners: {len(legal_corners)}")
            legal_moves = logic.find_legal_moves(self.board.grid, legal_corners, available_pieces, self.current_player.colour)
            print(f"Legal Moves: {len(legal_moves)}")
            # If no legal moves -> End Turn
            if len(legal_moves) == 0 and self.round != 1:
                self.current_player.finished = True
                print(f"{self.current_player.name} has no legal moves...")
                self.player_turn()
                return
        else:
            # AI player
            print(f"AI {self.current_player.name} is thinking...")
            available_pieces = self.current_player.remaining_pieces.copy()

            if self.round == 1:
            # Get starting squares
                match self.current_player.colour:
                    case 1: # Red starts in top-left
                        legal_corners = [[0,0]]
                    case 2: # Green starts in bottom-left but bottom-right if there are only 2 players
                        if self.no_of_players != 2:
                            legal_corners = [[self.board_size-1,0]]
                        else:
                            legal_corners = [[self.board_size-1,self.board_size-1]]
                    case 3: # Yellow starts in bottom-right
                        legal_corners = [[self.board_size-1,self.board_size-1]]
                    case 4: # Blue starts in top-right
                        legal_corners = [[0,self.board_size-1]]
                    case _:
                        raise ValueError("Invalid Colour")
                    
            else:
                legal_corners = logic.find_legal_corners(self.board.grid, self.current_player.colour)


            legal_moves = logic.find_legal_moves(self.board.grid, legal_corners, available_pieces, self.current_player.colour)
            # If no legal moves -> End Turn
            if len(legal_moves) != 0:
                print("AI found legal moves")
                # Get Move - move = [orientation, cell, piece]
                final_move = self.current_player.generate_move(legal_moves, self.board.grid, self.round) 

                # Remove piece from available pieces
                self.current_player.remaining_pieces.remove(final_move[2])

                # Place piece
                self.board.grid = logic.place_piece(self.board.grid, self.current_player.colour, final_move)

                self.player_turn()
            else:
                self.current_player.finished = True
                print(f"{self.current_player.name} has no legal moves...")
                self.player_turn()

            
        
