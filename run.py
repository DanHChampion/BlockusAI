# Import
import sys

from blockus.manager import Manager
from blockus.pygame import main

# Intialisation
args = sys.argv

# How many players
no_of_players = int(args[1]) # Min = 2, Max = 4

manager = Manager(no_of_players, ai_versions=["v1", "v3", "v1", "v2"])

# Display GUI?
try:
    gui = args[2]
    if gui == "GUI":
        main.run(manager)
except IndexError:
    manager.start_game()



