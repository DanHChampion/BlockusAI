# Import
import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('blockus/configurations/.env')
load_dotenv(dotenv_path=dotenv_path)

from blockus.manager import Manager
from blockus.pygame import main

# Intialisation
args = sys.argv

# How many players
no_of_players = int(args[1]) # Min = 2, Max = 4
AI_VERSIONS = json.loads(os.environ.get("AI_LIST"))
ALL_PIECES = json.loads(os.environ.get("ALL_PIECES"))


manager = Manager(no_of_players, ai_versions=AI_VERSIONS, available_pieces_types=ALL_PIECES)

# Display GUI?
try:
    gui = args[2]
    if gui == "GUI":
        main.run(manager)
except IndexError:
    manager.start_game()



