import math

BIG_BLOCK = "███"
BLOCK = "■"

def render_cell(value, item = BLOCK):
    match value:
        case 1:
            return f"\033[31m{item}\033[0m"
        case 2:
            return f"\033[32m{item}\033[0m"
        case 3:
            return f"\033[33m{item}\033[0m"
        case 4:
            return f"\033[34m{item}\033[0m"
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
    
    # Get max length of Player's names
    max_length = len(max([player_data[0] for player_data in data], key=len))
    if max_length < 6: max_length = 6

    print("+=========="+"="*max_length+"+")
    print("| Player "+" "*(max_length-6)+"| Score |")
    print("+=========="+"="*max_length+"+")
    for player_data in data:
        score = player_data[2]
        if score < 10:
            score = str(score)+ " "
        row = f"| {render_cell(int(player_data[1]), player_data[0])} "+" "*(max_length-len(player_data[0]))+f"| {score}    |"
        print(row)
        print("+=========="+"="*max_length+"+")