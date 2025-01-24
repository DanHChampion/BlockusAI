import math
import copy
from ..helpers import logic

# Heuristic parameters
CENTER_FACTOR = 5.0
EXPANSION_FACTOR = 5.0
BLOCK_OPPONENT_FACTOR = 6.0
PIECE_VALUE_FACTOR = 3.0
DIVERSITY_FACTOR = 2.0
SPACE_FACTOR = 1.5

def generate_move(legal_moves, board, round):
    fake_board = copy.deepcopy(board)
    best_move = legal_moves[0]
    best_score = evaluate_move(best_move, fake_board, round)

    for move in legal_moves[1:]:
        score = evaluate_move(move, fake_board, round)
        if score > best_score:
            best_move = move
            best_score = score

    return best_move


def evaluate_move(move, fake_board, round):
    board_size = len(fake_board)
    score = 0
    score += CENTER_FACTOR * score_point(move[1], board_size)
    fake_board = place_piece(fake_board, move)

    new_legal_corners = find_legal_corners(fake_board, move[2].colour)
    score += EXPANSION_FACTOR * len(new_legal_corners)
    score += DIVERSITY_FACTOR * evaluate_diversity(new_legal_corners, board_size)

    total_space = sum(calculate_space_around_point(fake_board, corner) for corner in new_legal_corners)
    score += SPACE_FACTOR * total_space

    opponent_colours = get_all_colours_from_board(fake_board, exclude=move[2].colour)
    for colour in opponent_colours:
        score -= BLOCK_OPPONENT_FACTOR * len(find_legal_corners(fake_board, colour))

    score += PIECE_VALUE_FACTOR * evaluate_piece_value(move[2])
    return score


def score_point(point, board_size):
    center = board_size / 2
    return 1 / (math.sqrt((center - point[0]) ** 2 + (center - point[1]) ** 2) + 1)


def evaluate_diversity(corners, board_size):
    regions = set((x // (board_size // 4), y // (board_size // 4)) for x, y in corners)
    return len(regions)

def calculate_space_around_point(board, point):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    x, y = point
    space = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 0:
            space += 1

    return space


def evaluate_piece_value(piece):
    return len(piece.piece[0]) * len(piece.piece)


def get_all_colours_from_board(board, exclude=None):
    return {cell for row in board for cell in row if cell and cell != exclude}


def place_piece(board, move):
    return logic.place_piece(board, move[2].colour, move)


def find_legal_corners(board, colour):
    return logic.find_legal_corners(board, colour)
