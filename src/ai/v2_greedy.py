import random

# Pick move with highest value
def generate_move(legal_moves, board, game_round):
    highest_value_moves = [legal_moves[0]]
    max_value = highest_value_moves[0][2].value

    for move in legal_moves:
        if move[2].value == max_value:
            highest_value_moves.append(move)
        elif move[2].value > max_value:
            max_value = move[2].value
            highest_value_moves = [move]

    return highest_value_moves[random.randint(0,len(highest_value_moves)-1)]