from . import v1_random
from . import v2_greedy

class AI():
    def __init__(self, version):
        self.version = version

    def generate_move(self, legal_moves, board):
        match self.version:
            case "v1":
                return v1_random.generate_move(legal_moves, board)
            case "v2":
                return v2_greedy.generate_move(legal_moves, board)
            case _:
                raise ValueError(self.version, "is not a existing version")

        
        