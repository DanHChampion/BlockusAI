from operator import itemgetter
import copy

from .helpers import draw

# Configurations
DEBUG = False
# Return the co-ordinates of all the corners where a cell of a piece can be placed


def is_cell_within_bounds(board, cell): # cell = [row,col]
    rows = cols = len(board)
    if 0 <= cell[0] < rows and 0 <= cell[1] < cols:
        return True
    return False

def is_cell_free(board, cell): # cell = [row,col]
    if is_cell_within_bounds(board, cell):
        if board[cell[0]][cell[1]] == 0:
            return True
    return False

def is_cell_adjacent_to_colour(board, cell, colour): # cell = [row,col]
    adj_cells = [
                    [cell[0] - 1,cell[1]],  # Top
                    [cell[0] + 1, cell[1]],  # Bottom
                    [cell[0], cell[1] - 1],  # Left
                    [cell[0], cell[1] + 1]   # Right
                ]
    for adj_cell in adj_cells:
        if is_cell_within_bounds(board, adj_cell):
            if get_cell_colour(board, adj_cell) == colour:
                return True
    return False

def get_cell_colour(board, cell):
    return board[cell[0]][cell[1]]

def find_legal_corners(board, colour):
    board_size = len(board)
    legal_corners = []        
    for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == colour:
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
                        if (is_cell_within_bounds(board, corner) and
                            is_cell_free(board, corner) and
                            not is_cell_adjacent_to_colour(board, corner, colour)):
                            legal_corners.append(corner)               
    
    return legal_corners

def find_legal_moves(board, legal_corners, available_pieces, colour):
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
                        if is_move_legal(board, move, colour, corner):
                            legal_moves.append(move)

    return legal_moves

def is_move_legal(board, move, colour, corner):
    test_board = copy.deepcopy(board)
    piece = move[0]
    cell = move[1]
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            current_cell = [row+cell[0], col + cell[1]]
            if piece[row][col]:
                if (not is_cell_within_bounds(board, current_cell) or
                    not is_cell_free(board, current_cell) or
                    is_cell_adjacent_to_colour(board, current_cell, colour)):
                    return False
                test_board[current_cell[0]][current_cell[1]] = 'D'
    
    if test_board[corner[0]][corner[1]] == 0:
        return False
    # draw._board(test_board)
    return True

def place_piece(board, colour, move):
    piece = move[0]
    cell = move[1]
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col]:
                board[row+cell[0]][col + cell[1]] = colour
    return board

def get_results(players_list, players_pieces):
    results = []
    for player in players_list:
        total = 0
        for piece in players_pieces[player.colour-1]:
            total += piece.value
        results.append([player.name, player.colour, total])

    # Sort 
    return sorted(results, key=itemgetter(2))
