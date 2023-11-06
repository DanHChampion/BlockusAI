from operator import itemgetter
import copy

from . import draw

# Configurations
DEBUG = False
# Return the co-ordinates of all the corners where a cell of a piece can be placed

class Logic:

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def is_cell_within_bounds(self, cell): # cell = [row,col]
        if 0 <= cell[0] < self.rows and 0 <= cell[1] < self.cols:
            return True
        return False
    
    def is_cell_free(self, cell): # cell = [row,col]
        if self.is_cell_within_bounds(cell):
            if self.board[cell[0]][cell[1]] == 0:
                return True
        return False
    
    def is_cell_adjacent_to_colour(self, cell, colour): # cell = [row,col]
        adj_cells = [
                        [cell[0] - 1,cell[1]],  # Top
                        [cell[0] + 1, cell[1]],  # Bottom
                        [cell[0], cell[1] - 1],  # Left
                        [cell[0], cell[1] + 1]   # Right
                    ]
        for adj_cell in adj_cells:
            if self.is_cell_within_bounds(adj_cell):
                if self.get_cell_colour(adj_cell) == colour:
                    return True
        return False
    
    def get_cell_colour(self, cell):
        return self.board[cell[0]][cell[1]]

    def find_legal_corners(self, colour):
        self.debug_board = self.board
        legal_corners = []        
        for row in range(self.rows):
                for col in range(self.cols):
                    if self.board[row][col] == colour:
                        # Look at corners
                        corners = [
                            [row - 1, col - 1],  # Top-left
                            [row - 1, col + 1],  # Top-right
                            [row + 1, col - 1],  # Bottom-left
                            [row + 1, col + 1]   # Bottom-right
                        ]
                        for corner in corners:
                            # If cell is:
                            #  Not within the board
                            #  Occupied
                            #  Adjacent to same colour
                            if (self.is_cell_within_bounds(corner) and
                                self.is_cell_free(corner) and
                                not self.is_cell_adjacent_to_colour(corner, colour)):
                                legal_corners.append(corner)               
        
        return legal_corners
    
    def find_legal_moves(self, legal_corners, available_pieces, colour):
        legal_moves = []
        # Generate moves given legal corners
        for corner in legal_corners:
            for piece in available_pieces:
                # Make move with piece and orientation
                orientations = piece.get_orientations()
                cell = corner
                # draw._pieces_in_row(orientations)
                for orientation in orientations:
                    # Translate the piece left then up
                    for row in range(len(orientation)):
                        for col in range(len(orientation[row])):
                            cell = [corner[0]-row, corner[1]- col]
                            move = [orientation, cell, piece]
                            if self.is_move_legal(move, colour, corner):
                                legal_moves.append(move)

        return legal_moves

    def is_move_legal(self, move, colour, corner):
        test_board = copy.deepcopy(self.board)
        piece = move[0]
        cell = move[1]
        for row in range(len(piece)):
            for col in range(len(piece[row])):
                current_cell = [row+cell[0], col + cell[1]]
                if piece[row][col]:
                    if (not self.is_cell_within_bounds(current_cell) or
                        not self.is_cell_free(current_cell) or
                        self.is_cell_adjacent_to_colour(current_cell, colour)):
                        return False
                    test_board[current_cell[0]][current_cell[1]] = 'D'
        
        if test_board[corner[0]][corner[1]] == 0:
            return False
        # draw._board(test_board)
        return True
    
    def place_piece(self, colour, move):
        piece = move[0]
        cell = move[1]
        for row in range(len(piece)):
            for col in range(len(piece[row])):
                if piece[row][col]:
                    self.board[row+cell[0]][col + cell[1]] = colour
    
    def get_results(self, players_list, players_pieces):
        results = []
        for player in players_list:
            total = 0
            for piece in players_pieces[player.colour-1]:
                total += piece.value
            results.append([player.name, player.colour, total])

        # Sort 
        return sorted(results, key=itemgetter(2))
