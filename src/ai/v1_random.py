import random

#Pick random move
def generate_move(legal_moves, board, game_round):
    return legal_moves[random.randint(0,len(legal_moves)-1)]
