import random
import math
import copy

from ..logic import Logic

# Parameters
CORNER_FACTOR = 6.0
CORNERS_FACTOR = 0.3

def generate_move(legal_moves, board, round):
    # Pick move with highest value and allows players to move closer towards center
    fake_board = copy.deepcopy(board)
    logic = Logic(fake_board)

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
    best_move_score = evaluate_move(best_move, logic)
    for move in highest_value_moves[1:]:
        current_move_score = evaluate_move(move, logic)
        if  current_move_score > best_move_score:
            best_move = move
            best_move_score = current_move_score
    
    return best_move


def evaluate_move(move, logic):
    board_size = logic.rows
    score = CORNER_FACTOR * score_point(move[1], board_size)

    # Fake move
    logic.place_piece(move[2].colour, move)

    new_legal_corners = logic.find_legal_corners(move[2].colour)

    # Score each new legal corner
    for corner in new_legal_corners:
        score += CORNERS_FACTOR * score_point(corner, board_size)

    return score

def score_point(point, board_size):
    return 1/math.sqrt(math.pow((board_size/2)-point[0],2)+math.pow((board_size/2)-point[1],2))
