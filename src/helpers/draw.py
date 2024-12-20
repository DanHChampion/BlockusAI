import math
from operator import itemgetter
from colorama import init, Fore, Style

# Initialize colorama (Windows only)
init(convert=True)

BIG_BLOCK = "███"
BLOCK = "■"

def render_cell(value, item = BLOCK):
    match value:
        case 1:
            return f"{Fore.RED}{item}{Style.RESET_ALL}"
        case 2:
            return f"{Fore.GREEN}{item}{Style.RESET_ALL}"
        case 3:
            return f"{Fore.YELLOW}{item}{Style.RESET_ALL}"
        case 4:
            return f"{Fore.BLUE}{item}{Style.RESET_ALL}"
        case 'D': # Debugging Purposes
            return " # "
        case _:
            return "   "

def _piece(piece):
    for row in piece:
        for cell in row:
            if cell:
                print(render_cell(cell), end=" ")
            else:
                print(" ", end=" ")
        print()
    print("")

def _pieces_in_row(pieces):
    # Make list of pieces into a massive 2D Array
    arr = []
    for i in range(5):
        row_list = []
        for piece in pieces:
            try:
                row_list.extend(piece[i])
            except IndexError:
                row_list.extend([0 for _ in range(len(piece[0]))])
            row_list.append(0)
        arr.append(row_list)
    _piece(arr)

def _board(data):
    rows = len(data)
    cols = len(data[0])
    for row in range(0,rows*2 + 1):
        string = ""
        if (row%2 == 0):
            string = ("+---")*cols +"+"
            print(string)
            continue
        for col in range(0,cols):
            string += "|"+ render_cell(data[math.floor(row/2)][col], BIG_BLOCK)
        print(string +"|")

def _results(data):
    # Sort data by the score (item at index 2)
    data = sorted(data, key=itemgetter(2))

    # Get max length of Player's names
    max_name_length = len(max([player_data[0] for player_data in data], key=len))
    if max_name_length < 6:
        max_name_length = 6

    # Set fixed width for AI Version
    max_version_length = 10  # "AI Version" header length

    # Get max length of remaining pieces strings
    max_remaining_pieces_length = max(len(", ".join([piece.type for piece in player_data[4]])) for player_data in data)

    # Ensure a minimum width for remaining pieces
    if max_remaining_pieces_length < 20:
        max_remaining_pieces_length = 20

    # Print table header
    print("+==" + "=" * max_name_length + "+=======+=" + "=" * max_version_length + "=+" + "=" * (max_remaining_pieces_length + 2) + "+")
    print(f"| Player{' ' * (max_name_length - 6)} | Score | AI Version | Remaining Pieces{' ' * (max_remaining_pieces_length - 16)} |")
    print("+==" + "=" * max_name_length + "+=======+=" + "=" * max_version_length + "=+" + "=" * (max_remaining_pieces_length + 2) + "+")

    # Print each player's data
    for player_data in data:
        player_name = render_cell(int(player_data[1]), player_data[0])
        score = str(player_data[2]).ljust(5)  # Ensure score is aligned
        ai_version = player_data[3].ljust(max_version_length)
        
        # Extract piece types from remaining_pieces
        remaining_pieces = ", ".join([piece.type for piece in player_data[4]])

        # Format the row
        row = f"| {player_name}{' ' * (max_name_length - len(player_data[0]))} | {score} | {ai_version} | {remaining_pieces.ljust(max_remaining_pieces_length)} |"
        print(row)
        print("+==" + "=" * max_name_length + "+=======+=" + "=" * max_version_length + "=+" + "=" * (max_remaining_pieces_length + 2) + "+")
