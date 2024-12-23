from .agent import DQNAgent
from .wrapper import BlokusWrapper
from ...helpers import logic
from ...configurations.config import configuration
from ...helpers import draw

def run(manager):
    env = BlokusWrapper(manager)

    