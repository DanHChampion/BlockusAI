import random
import math
import copy

from .. import logic
from . import v2_greedy

# Parameters
CORNER_FACTOR = 6.0
CORNERS_FACTOR = 0.3

def generate_move(legal_moves, board, round):
    # Pick move with highest value and allows players to move closer towards center
    
    if round <= 5:
        fake_board = copy.deepcopy(board)

        highest_value_moves = [legal_moves[0]]
        max_value = highest_value_moves[0][2].value

        for move in legal_moves:
            if move[2].value == max_value:
                highest_value_moves.append(move)
            elif move[2].value > max_value:
                max_value = move[2].value
                highest_value_moves = [move]

        # Evaluate moves
        best_move = highest_value_moves[0]
        best_move_score = evaluate_move(best_move, fake_board)
        for move in highest_value_moves[1:]:
            current_move_score = evaluate_move(move, fake_board)
            if  current_move_score > best_move_score:
                best_move = move
                best_move_score = current_move_score

        return best_move
    
    return v2_greedy.generate_move(legal_moves, board, round)


def evaluate_move(move, fake_board):
    board_size = len(fake_board)
    score = CORNER_FACTOR * score_point(move[1], board_size)

    # Fake move
    fake_board = logic.place_piece(fake_board, move[2].colour, move)

    new_legal_corners = logic.find_legal_corners(fake_board, move[2].colour)

    # Score each new legal corner
    for corner in new_legal_corners:
        score += CORNERS_FACTOR * score_point(corner, board_size)

    return score


def score_point(point, board_size):
    return 1/math.sqrt(math.pow((board_size/2)-point[0],2)+math.pow((board_size/2)-point[1],2))
