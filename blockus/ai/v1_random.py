import random

def generate_move(legal_moves, board, round):
    #Pick random move
    move = legal_moves[random.randint(0,len(legal_moves)-1)]

    return move