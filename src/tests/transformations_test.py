# tests/test_draw.py
from helpers.transformations import rotate_piece_clockwise, flip_piece_vertical, set_colour
import pytest

def test_rotate_90():
    piece = [[1, 0], [0, 1]]
    expected = [[0, 1], [1, 0]]
    assert rotate_piece_clockwise(piece, 1) == expected

def test_flip_vertical():
    piece = [[1, 0], [0, 1]]
    expected = [[0, 1], [1, 0]]
    assert flip_piece_vertical(piece) == expected

def test_set_colour_red():
    piece = [[1, 0], [0, 1]]
    expected = [[1, 0], [0, 1]]
    assert set_colour(piece, 1) == expected

def test_set_colour_invalid():
    with pytest.raises(ValueError):
        set_colour([[1]], 5)
