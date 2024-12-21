# Import
import json
import argparse

from src.manager import Manager
from src.pygame import main as pygame_main
from src.web import app as web_app
from src.experiment import experiment

from src.configurations.config import configuration

# Intialisation
parser = argparse.ArgumentParser(
                    prog='Blockus',
                    description='Blockus AI')

parser.add_argument('--phase')
parser.add_argument('--players')

args = parser.parse_args()

# How many players
no_of_players = int(args.players) # Min = 2, Max = 4
if not (no_of_players == 2 or no_of_players == 4):
    raise ValueError("Must be 2 or 4 players")
AI_VERSIONS = json.loads(configuration.AI_LIST)
if (len(AI_VERSIONS) < no_of_players):
    raise ValueError(f"AI_LIST should include at least {no_of_players} values")
ai_versions = AI_VERSIONS[:no_of_players]
ALL_PIECES = json.loads(configuration.ALL_PIECES)


manager = Manager(no_of_players, ai_versions=ai_versions, available_pieces_types=ALL_PIECES)

match args.phase:
    case "CLI":
        manager.start_game()
    case "GUI":
        pygame_main.run(manager)
    case "WEB":
        web_app.run()
    case "EXP":
        experiment.run(manager)
    case _:
        raise RuntimeError("Invalid Phase")




