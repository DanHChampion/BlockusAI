import math
import copy
from ..helpers import logic

# Heuristic parameters based on limited testing
CENTER_WEIGHT = 5.0
EXPANSION_WEIGHT = 4.0
BLOCK_OPPONENT_WEIGHT = 6.0
PIECE_VALUE_WEIGHT = 3.0

# Pick move with highest score based on evaluation function
def generate_move(legal_moves, board, game_round):
    simulated_board = copy.deepcopy(board)
    best_move = legal_moves[0]
    highest_score = evaluate_move(best_move, simulated_board, game_round)

    for move in legal_moves[1:]:
        current_score = evaluate_move(move, simulated_board, game_round)
        if current_score > highest_score:
            best_move = move
            highest_score = current_score

    return best_move

# Evaluates a move using a heuristic scoring system.
def evaluate_move(move, simulated_board, game_round):
    board_size = len(simulated_board)
    score = 0

    # Score based on proximity to the center
    score += CENTER_WEIGHT * calculate_center_proximity(move[1], len(simulated_board))

    # Simulate placing the piece on the board
    simulated_board = logic.place_piece(simulated_board, move[2].colour, move)

    # Score based on expansion potential
    new_legal_corners = logic.find_legal_corners(simulated_board, move[2].colour)
    score += EXPANSION_WEIGHT * len(new_legal_corners)

    # Penalize based on blocking opponent's moves
    opponent_colours = get_all_player_colours(simulated_board, exclude=move[2].colour)
    for colour in opponent_colours:
        score -= BLOCK_OPPONENT_WEIGHT * len(logic.find_legal_corners(simulated_board, colour))

    # Score based on piece value
    score += PIECE_VALUE_WEIGHT * calculate_piece_value(move[2], game_round)

    return score

# Calculates a score based on the proximity of a point to the center of the board.
def calculate_center_proximity(point, board_size):
    center = board_size / 2
    return 1 / (math.sqrt((center - point[0]) ** 2 + (center - point[1]) ** 2) + 1)

# Calculates a score based on the area of the piece and the game round.
def calculate_piece_value(piece, game_round):
    return piece.value * (1.5 if game_round <= 6 else 0.8)

# Retrieves all unique player colours present on the board, excluding a specific colour if provided.
def get_all_player_colours(board, exclude=None):
    return {cell for row in board for cell in row if cell and cell != exclude}

