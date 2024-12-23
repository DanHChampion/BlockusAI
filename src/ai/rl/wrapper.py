from ...helpers import logic
from ...helpers import draw

BLOCK_FACTOR = 2

class BlokusWrapper:
    def __init__(self, manager):
        self.manager = manager

    def reset(self):
        self.manager.intialise(
            no_of_players=self.manager.no_of_players,
            available_pieces_types=self.manager.available_pieces_types,
            ai_versions=self.manager.ai_versions,
            shuffle=False,
        )
        return self.get_state()

