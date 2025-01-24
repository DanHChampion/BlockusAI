import csv

from ..manager import Manager
from ..configurations.config import configuration

# allow experiment parameters

# NoOfGames per rotation
# Rotate Position (True False)
# AI_LIST what versions


# run all the games
# with different parameters


# Record ALL results as csv
# NoOfGames won
# At which position (colour)
# finish at what rank
# score at the end of each game
# what piece player had left
# time taken for game to finish
# what round finish on

NO_OF_GAMES_PER_SET = configuration.GAMES
ROTATE_COLOURS = True
RECORD = configuration.RECORD

def run(manager):
    # Intialise game
    SETS = 4 if ROTATE_COLOURS else 1
    print (SETS)

    no_of_players = manager.no_of_players
    available_pieces_types = manager.available_pieces_types
    ai_versions = manager.ai_versions

    for set in range(1,SETS+1):
        for game in range(1,NO_OF_GAMES_PER_SET+1):
            print (f"Set: {set} Game: {game}")
            current_manager = Manager(no_of_players, available_pieces_types, ai_versions)
            current_manager.start_game()
            results = current_manager.get_results()
            # Record Results in CSV
            if RECORD:
                file_name = "results.csv"

                # Check if the file exists and write headers if not
                try:
                    with open(file_name, "x", newline="") as f:  # Use "x" to create the file
                        writer = csv.writer(f)
                        writer.writerow(["Player", "Colour", "Score", "AI Version", "Remaining Pieces"])
                except FileExistsError:
                    pass  # File already exists; no need to write headers

                # Write game results to the file
                with open(file_name, "a", newline="") as f:
                    writer = csv.writer(f)
                    for player_result in results:
                        player_name = player_result[0]
                        player_colour = player_result[1]
                        player_score = player_result[2]
                        ai_version = player_result[3]
                        remaining_pieces = ",".join(piece.type for piece in player_result[4])
                        writer.writerow([player_name, player_colour, player_score, ai_version, remaining_pieces])

                print(f"Results saved to {file_name}")