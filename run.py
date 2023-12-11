# Import
import sys
import json
import argparse


from src.manager import Manager
from src.pygame import main as pygame_main
from src.web import main as web_main

from src.configurations.config import configuration


# print(Config)

# Intialisation
parser = argparse.ArgumentParser(
                    prog='Blockus',
                    description='Blockus AI',
                    epilog='Text at the bottom of help')

parser.add_argument('--phase')
parser.add_argument('--players')

args = parser.parse_args()

# How many players
no_of_players = int(args.players) # Min = 2, Max = 4
if not (no_of_players == 2 or no_of_players == 4):
    raise ValueError("Must be 2 or 4 players")
AI_VERSIONS = json.loads(configuration.AI_LIST)
if (len(AI_VERSIONS) != no_of_players):
    raise ValueError(f"AI_LIST should include {no_of_players} values")
ALL_PIECES = json.loads(configuration.ALL_PIECES)

manager = Manager(no_of_players, ai_versions=AI_VERSIONS, available_pieces_types=ALL_PIECES)

match args.phase:
    case "CLI":
        manager.start_game()
    case "GUI":
        pygame_main.run(manager)
    case "WEB":
        web_main.run()
    case _:
        raise RuntimeError("Invalid Phase")




