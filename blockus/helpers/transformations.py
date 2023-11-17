# Rotate a piece clockwise (90deg)
def rotate_piece_clockwise(piece, no_of_rotations):
    rotated_piece = piece
    rows = len(piece)
    cols = len(piece[0])
    for _ in range(no_of_rotations % 4):
        # Initialize an empty rotated piece with the new dimensions
        rotated_piece = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                rotated_piece[col][rows - 1 - row] = piece[row][col]

        piece = rotated_piece
        rows, cols = cols, rows  # Update dimensions after rotation

    return rotated_piece

# Flip a piece vertically
def flip_piece_vertical(piece):
    flipped_piece = piece[::-1]
    return flipped_piece

def set_colour(piece, colour):
    # Red = 1
    # Green = 2
    # Yellow = 3
    # Blue = 4
    if colour > 4:
        raise ValueError('Colour must be between 1-4')
    multiplied_array = [[cell * colour for cell in row] for row in piece]
    return multiplied_array