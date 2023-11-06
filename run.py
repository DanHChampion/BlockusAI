# Import
import sys

from blockus.manager import Manager

# Intialisation
args = sys.argv

# How many players
no_of_players = int(args[1]) # Min = 2, Max = 4


manager = Manager(no_of_players, ai_versions=["v2", "v1", "v1", "v1"])

manager.start_game()