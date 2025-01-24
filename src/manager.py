# Import
import time
import random
import csv

from .configurations.config import configuration
from .helpers import logic
from .helpers.piece import Piece
from .helpers.player import Player
from .helpers import draw

VERBOSITY = configuration.VERBOSITY
DRAW = configuration.DRAW
DRAW_RESULTS = configuration.DRAW_RESULTS
STEP_BY_STEP = configuration.STEP_BY_STEP
MAX_ROUNDS = configuration.MAX_ROUNDS
RECORD = configuration.RECORD

class Manager:
    def __init__(self, no_of_players, available_pieces_types = None, ai_versions = None, shuffle = False):
        self.intialise(no_of_players, available_pieces_types, ai_versions, shuffle)
        
    def intialise(self, no_of_players, available_pieces_types, ai_versions, shuffle):
        # Initialise Game
        self.round = 0
        self.turn = 0
        # Check if input values are correct
        
        # If AI versions aren't specified
        if ai_versions is None:
            ai_versions = ["v1" for _ in range(1,no_of_players+1)]
        self.ai_versions = ai_versions

        # Players
        if not (no_of_players == 2 or no_of_players == 4):
            raise ValueError("Must be 2 or 4 players")
        self.no_of_players = no_of_players
        self.player_list = [Player(player, self.ai_versions[player-1]) for player in range(1,no_of_players+1)]
        
        if shuffle:
            random.shuffle(self.player_list)

        # Generate Board
        self.board_size = 3*no_of_players + 8
        self.board = [[ 0 for x in range(0,self.board_size)] for y in range(0,self.board_size)]

        # Generate Pieces for players
        self.available_pieces_types = available_pieces_types
        self.player_pieces = []
        for player in self.player_list:
            player.remaining_pieces = [Piece(piece_type,player.colour) for piece_type in available_pieces_types]

        self.start_time = time.time()


    def start_game(self):
        print(f"Starting game with {self.no_of_players} players...")
        flag = True
        # Game Loop
        while(flag):
            self.round += 1
            self.output_text(f"Round: {self.round}")
            flag = False
            for player in self.player_list:
                if self.player_turn(player):
                    flag = True
            if STEP_BY_STEP: 
                draw._board(self.board)
                input("")
            if self.round == MAX_ROUNDS: break
        self.end_game()

    def end_game(self):
        runtime = format(time.time()-self.start_time,".2f")
        print("Showing results...")
        print(f"Game finished after {runtime}s") # Print how long game took
        print(f"Played a total of {self.round} rounds")

        if DRAW_RESULTS:
            # Show final state of board
            draw._board(self.board)
            # Show Remaining Pieces
            self.output_text("\nRemaining Pieces:")
            for player in self.player_list:
                pieces_list = [_.piece for _ in player.remaining_pieces]
                draw._pieces_in_row(pieces_list)

        # Show Results
        results = self.get_results()
        draw._results(results)
        

    def player_turn(self, player):
        player_string = draw.render_cell(player.colour, str(player))
        self.turn += 1

        # If player finished -> End Turn
        if player.finished:
            self.output_text(f"{player_string} is finished...")
            return False

        # If no pieces left -> End Turn
        available_pieces = player.remaining_pieces
        if len(available_pieces) == 0:
            player.finished = True
            self.output_text(f"{player_string} has no more pieces...")
            return False
        
        if DRAW: 
            print(f"{player_string}'s available pieces:")
            draw._pieces_in_row([_.piece for _ in available_pieces])

        if self.round == 1:
            # Get starting squares
            match player.colour:
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
            # If no corners to place piece -> End Turn
            legal_corners = logic.find_legal_corners(self.board, player.colour)
            if len(legal_corners) == 0:
                player.finished = True
                self.output_text(f"{player_string} has no legal moves...")
                return False
        
        # Get all possible moves
        legal_moves = logic.find_legal_moves(self.board, legal_corners, available_pieces, player.colour)
        # If no legal moves -> End Turn
        if len(legal_moves) == 0: 
            player.finished = True
            self.output_text(f"{player_string} has no legal moves...")
            return False
        
        # Get Move - move = [orientation, cell, piece]
        final_move = player.generate_move(legal_moves, self.board, self.round)
       
        self.output_text(f"{player_string} placed {final_move[2]} at {final_move[1]}")
        if DRAW:
            draw._piece(final_move[0])

        # Remove piece from available pieces
        player.remaining_pieces.remove(final_move[2])

        # Place piece
        self.board = logic.place_piece(self.board, player.colour, final_move)

        # End Turn
        return True
    
    def output_text(self, text):
        if VERBOSITY: print(text)

    def get_results(self):
        return logic.calc_results(self.player_list)


