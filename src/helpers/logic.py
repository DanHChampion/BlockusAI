def is_cell_within_bounds(board, cell): # cell = [row,col]
    rows = cols = len(board)
    if 0 <= cell[0] < rows and 0 <= cell[1] < cols:
        return True
    return False

def is_cell_free(board, cell): # cell = [row,col]
    if is_cell_within_bounds(board, cell):
        if get_cell_colour(board, cell) == 0:
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
    for corner in legal_corners:
        for piece in available_pieces:
            orientations = piece.get_orientations()
            for orientation in orientations:
                for row_offset in range(len(orientation)):
                    for col_offset in range(len(orientation[row_offset])):
                        if orientation[row_offset][col_offset]:  # Check if this cell of the piece is occupied
                            cell = [corner[0] - row_offset, corner[1] - col_offset]
                            move = [orientation, cell, piece]
                            if is_move_legal(board, move, colour, legal_corners):
                                legal_moves.append(move)
    return legal_moves

def is_move_legal(board, move, colour, legal_corners):
    # Check if the piece has at least one tile on a legal corner
    piece = move[0]
    cell = move[1]
    legal = False

    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col]:  # Check if this cell of the piece is occupied
                current_cell = [cell[0] + row, cell[1] + col]

                # Check if the cell is within bounds and free
                if not is_cell_within_bounds(board, current_cell) or not is_cell_free(board, current_cell):
                    return False

                # Check if the cell is adjacent to the same colour
                if is_cell_adjacent_to_colour(board, current_cell, colour):
                    return False

                # Check if the piece has at least one tile on a legal corner
                if current_cell in legal_corners:
                    legal = True

    return legal

def place_piece(board, colour, move):
    piece = move[0]
    cell = move[1]
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col]:
                board[row+cell[0]][col + cell[1]] = colour
    return board

def get_starting_corner(board_size, colour):
    match colour:
        case 1: # Red starts in top-left
            return [[0,0]]
        case 2: # Green starts in top-right
            return [[0,board_size-1]]
        case 3: # Yellow starts in bottom-right
            return [[board_size-1,board_size-1]]
        case 4: # Blue starts in bottom-left
            return [[board_size-1,0]]
        case _:
            raise ValueError("Invalid Colour")

def calc_results(players_list):
    results = []
    for player in players_list:
        results.append([player.name, player.colour, player.current_score(), player.ai_version, player.remaining_pieces])
    return results
