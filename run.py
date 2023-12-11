# Import
import sys
import json


from src.manager import Manager
from src.pygame import main as pygame_main
from src.web import main as web_main

from src.configurations.config import configuration


# print(Config)

# Intialisation
args = sys.argv

# How many players
no_of_players = int(args[1]) # Min = 2, Max = 4
if not (no_of_players == 2 or no_of_players == 4):
    raise ValueError("Must be 2 or 4 players")
AI_VERSIONS = json.loads(configuration.AI_LIST)
if (len(AI_VERSIONS) != no_of_players):
    raise ValueError(f"AI_LIST should include {no_of_players} values")
ALL_PIECES = json.loads(configuration.ALL_PIECES)

manager = Manager(no_of_players, ai_versions=AI_VERSIONS, available_pieces_types=ALL_PIECES)

# Display GUI?
try:
    phase = args[2]
    if phase == "GUI":
        pygame_main.run(manager)
    elif phase == "WEB":
        web_main.run()
except IndexError:
    manager.start_game()



