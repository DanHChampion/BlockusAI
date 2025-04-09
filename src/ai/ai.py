from . import v1_random
from . import v2_greedy
from . import v3_evaluator
from . import v4_chatgpt
from . import v5_champion

class AI():
    def __init__(self, version):
        self.version = version

    def generate_move(self, legal_moves, board, round):
        match self.version:
            case "v1":
                return v1_random.generate_move(legal_moves, board, round)
            case "v2":
                return v2_greedy.generate_move(legal_moves, board, round)
            case "v3":
                return v3_evaluator.generate_move(legal_moves, board, round)
            case "v4":
                return v4_chatgpt.generate_move(legal_moves, board, round)
            case "v5":
                return v5_champion.generate_move(legal_moves, board, round)
            case "hm":
                return None
            case _:
                raise ValueError(f"'{self.version}' is not a valid version")

        
        