import gymnasium as gym
import numpy as np
from gymnasium import spaces

from ...configurations.constants import BOARD_SIZE, NUM_PLAYERS, ALL_PIECES

class BlokusEnv(gym.Env):
    def __init__(self):
        super(BlokusEnv, self).__init__()

        # Define the observation space: the board state and the pieces each player has
        self.observation_space = spaces.Dict({
            'board': spaces.Box(low=0, high=NUM_PLAYERS, shape=(BOARD_SIZE, BOARD_SIZE), dtype=np.int8),
            'pieces': spaces.MultiBinary(len(ALL_PIECES) * NUM_PLAYERS),
            'current_player': spaces.MultiBinary(NUM_PLAYERS)
        })
        
        self.reset()