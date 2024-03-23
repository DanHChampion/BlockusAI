from ..manager import Manager

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

NO_OF_GAMES_PER_SET = 1
ROTATE_COLOURS = True

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
            print(current_manager.get_results())