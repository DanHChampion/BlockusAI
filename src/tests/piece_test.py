import pytest
from helpers.transformations import rotate_piece_clockwise, flip_piece_vertical
from helpers.draw import _piece  # This can be mocked if needed
from helpers.piece import Piece  # Assuming the piece class is located in the 'piece' module

# Mock piece to test drawing functionality
@pytest.fixture
def mock_piece():
    return Piece("I1", 1)  # Simple piece to test functionality

# Test piece initialization
def test_piece_initialization():
    piece = Piece("I1", 1)
    assert piece.type == "I1"
    assert piece.colour == 1
    assert piece.value == 1
    assert piece.piece == [[1]]  # For type "I1", the piece should be a 1x1 matrix

# Test get_orientations for simple pieces
def test_get_orientations_simple_piece():
    piece = Piece("I1", 1)
    orientations = piece.get_orientations()
    assert len(orientations) == 1  # I1 has only one orientation
    assert orientations[0] == [[1]]  # It should match the original piece shape

def test_get_orientations_rotate_2():
    piece = Piece("I2", 1)
    orientations = piece.get_orientations()
    assert len(orientations) == 2  # I2 has two orientations
    assert orientations[1] == [[1], [1]]  # The second orientation should be rotated 90 degrees

# Test for pieces that have more orientations (e.g., "T", "L", "Z")
def test_get_orientations_complex_piece():
    piece = Piece("T4", 1)
    orientations = piece.get_orientations()
    assert len(orientations) == 4  # T4 has four possible orientations
    assert orientations[0] == [[0, 1, 0], [1, 1, 1]]  # Check initial orientation
    assert orientations[1] == [[1, 0], [1, 1], [1, 0]]  # Check 90 degree rotated orientation

def test_get_orientations_flip_and_rotate():
    piece = Piece("Z4", 1)
    orientations = piece.get_orientations()
    assert len(orientations) == 4  # Z4 has four orientations
    assert orientations[2] == [[1, 1, 0], [0, 1, 1]]  # Check flipped orientation

# Test for piece assignment (whether correct piece is assigned based on type)
def test_assign_piece():
    piece = Piece("I1", 1)
    assert piece.value == 1
    assert piece.piece == [[1]]

    piece = Piece("T4", 1)
    assert piece.value == 4
    assert piece.piece == [[0, 1, 0], [1, 1, 1]]

# Test the __str__ method for Piece
def test_piece_str():
    piece = Piece("I1", 1)
    assert str(piece) == "I1"

# Test draw_piece method
def test_draw_piece(mock_piece):
    # Assuming we have a mock or a real implementation for _piece function
    mock_piece.draw_piece()
    # If the `draw._piece` function prints something or updates some state, we would check it here.
    # For now, we'll assume this works if no errors occur during the function call.

# Test for ValueError when an invalid piece type is provided
def test_invalid_piece_type():
    with pytest.raises(ValueError):
        Piece("InvalidType", 1)

# Test for handling piece transformations (rotate and flip)
def test_transformations():
    piece = Piece("I1", 1)
    rotated = rotate_piece_clockwise(piece.piece, 1)
    flipped = flip_piece_vertical(piece.piece)

    # I1 is a 1x1 piece, so rotations and flips should return the same thing
    assert rotated == piece.piece
    assert flipped == piece.piece

# Test that the get_orientations function handles all types correctly
@pytest.mark.parametrize("piece_type, expected_orientation_count", [
    ("I1", 1),
    ("I2", 2),
    ("T4", 4),
    ("Z4", 4),
    ("L4", 8),
    ("X", 1)
])
def test_get_orientations_parametrized(piece_type, expected_orientation_count):
    piece = Piece(piece_type, 1)
    orientations = piece.get_orientations()
    assert len(orientations) == expected_orientation_count
