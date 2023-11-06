# Import
import sys

from blockus.manager import Manager
from blockus.pygame import display

# Intialisation
args = sys.argv

# How many players
no_of_players = int(args[1]) # Min = 2, Max = 4

# Display GUI?
gui = args[2]

manager = Manager(no_of_players, ai_versions=["v2", "v2", "v3", "v2"])

if gui == "GUI":
    display.display(manager)

manager.start_game()