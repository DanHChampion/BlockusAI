from ..ai.ai import AI

class Player:
    def __init__(self, colour, ai = "v1", name = None):
        self.colour = colour

        if name is None:
            match colour:
                case 1:
                    self.name = "Red"
                case 2:
                    self.name = "Green"
                case 3:
                    self.name = "Yellow"
                case 4:
                    self.name = "Blue"
                case _:
                    raise ValueError(colour, "is not a colour")
        
        self.ai = AI(ai)
        self.ai_version = ai
        self.finished = False
        self.remaining_pieces = []

    def __str__(self):
        return self.name

    def generate_move(self, legal_moves, board, round):
        return self.ai.generate_move(legal_moves, board, round)
    
    def current_score(self):
        return sum(piece.value for piece in self.remaining_pieces)


