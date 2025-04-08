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
parser.add_argument('--players', required=False, default=4)
parser.add_argument('--shuffle', required=False, default=False)

args = parser.parse_args()

# How many players
no_of_players = int(args.players) # Min = 2, Max = 4
if not (no_of_players == 2 or no_of_players == 4):
    raise ValueError("Must be 2 or 4 players")
AI_VERSIONS = json.loads(configuration.AI_LIST)
if (len(AI_VERSIONS) < no_of_players):
    raise ValueError(f"AI_LIST should include at least {no_of_players} values. Please update your .env file")
ai_versions = AI_VERSIONS[:no_of_players]
ALL_PIECES = json.loads(configuration.ALL_PIECES)
SHUFFLE = bool(args.shuffle)

manager = Manager(
    no_of_players,
    ai_versions=ai_versions,
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




