from .ai.ai import AI

class Player:
    def __init__(self, colour, ai = "v1", name = None):
        self.colour = colour

        if name is None:
            match colour:
                case 1:
                    self.name = "Apple"
                case 2:
                    self.name = "Lime"
                case 3:
                    self.name = "Banana"
                case 4:
                    self.name = "Blueberry"
                case _:
                    raise ValueError(colour, "is not a colour")
        
        self.ai = AI(ai)
        self.finished = False

    def __str__(self):
        return self.name

    def generate_move(self, legal_moves, board, round):
        return self.ai.generate_move(legal_moves, board, round)


