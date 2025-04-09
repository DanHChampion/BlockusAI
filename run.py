# Import
import json
import argparse

from src.manager import Manager
from src.gui import main as pygame_gui
from src.game import main as pygame_main
from src.experiment import experiment
from src.ai.rl import training

from src.configurations.config import configuration

# Intialisation
parser = argparse.ArgumentParser(
                    prog='Blockus',
                    description='Blockus AI')

parser.add_argument('--phase')
parser.add_argument('--shuffle', required=False, default=False)

args = parser.parse_args()

AI_VERSIONS = json.loads(configuration.AI_LIST)
ALL_PIECES = json.loads(configuration.ALL_PIECES)
SHUFFLE = bool(args.shuffle)

manager = Manager(
    ai_versions=AI_VERSIONS,
    available_pieces_types=ALL_PIECES,
    shuffle=SHUFFLE
)

match args.phase:
    case "CLI":
        manager.start_game()
    case "GUI":
        pygame_gui.run(manager)
    case "GAME":
        pygame_main.main()
    case "EXP":
        experiment.run(manager)
    case "DQN":
        training.run(manager)
    case _:
        raise RuntimeError("Invalid Phase")




