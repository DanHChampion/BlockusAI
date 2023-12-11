from . import transformations
from . import draw

class Piece:
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour
        piece, self.value = self.assign_piece(type)
        self.piece = transformations.set_colour(piece, colour)
        self.orientations = []
        self.translations = []

    def __str__(self):
        return f"{self.type}"

    def draw_piece(self):
        draw._piece(self.piece)

    def get_orientations(self):
        match self.type:
            case "I1" | "O4" | "X":
                return [self.piece]
            case "I2" | "I3" | "I4" | "I5":
                return [self.piece, 
                        transformations.rotate_piece_clockwise(self.piece, 1)]
            case "V3" | "T4" | "U" | "W" | "T" | "V5":
                return [self.piece, 
                        transformations.rotate_piece_clockwise(self.piece, 1),
                        transformations.rotate_piece_clockwise(self.piece, 2),
                        transformations.rotate_piece_clockwise(self.piece, 3)]
            case "Z4" | "Z5":
                return [self.piece, 
                        transformations.rotate_piece_clockwise(self.piece, 1),
                        transformations.flip_piece_vertical(self.piece),
                        transformations.flip_piece_vertical(transformations.rotate_piece_clockwise(self.piece, 1))]
            case "L4" | "Y" | "L5" | "N" | "F" | "P":
                return [self.piece, 
                        transformations.rotate_piece_clockwise(self.piece, 1),
                        transformations.rotate_piece_clockwise(self.piece, 2),
                        transformations.rotate_piece_clockwise(self.piece, 3),
                        transformations.flip_piece_vertical(self.piece),
                        transformations.flip_piece_vertical(transformations.rotate_piece_clockwise(self.piece, 1)),
                        transformations.flip_piece_vertical(transformations.rotate_piece_clockwise(self.piece, 2)),
                        transformations.flip_piece_vertical(transformations.rotate_piece_clockwise(self.piece, 3))]
            case _:
                raise ValueError(self.type,"is not a piece")

    def assign_piece(self, type):
        match type:
            case "I1":
                return piece_i1,1
            case "I2":
                return piece_i2,2
            case "I3":
                return piece_i3,3
            case "I4":
                return piece_i4,4
            case "I5":
                return piece_i5,5
            case "V3":
                return piece_v3,3
            case "O4":
                return piece_o4,4
            case "Z4":
                return piece_z4,4
            case "T4":
                return piece_t4,4
            case "L4":
                return piece_l4,4
            case "U":
                return piece_u,5
            case "P":
                return piece_p,5
            case "L5":
                return piece_l5,5
            case "N":
                return piece_n,5
            case "Y":
                return piece_y,5
            case "X":
                return piece_x,5
            case "W":
                return piece_w,5
            case "F":
                return piece_f,5
            case "Z5":
                return piece_z5,5
            case "T":
                return piece_t,5
            case "V5":
                return piece_v5,5
            case _:
                raise ValueError(type,"is not a piece")


# Basic Pieces
piece_i1 = [[1]]
piece_i2 = [[1,1]]
piece_i3 = [[1,1,1]]
piece_i4 = [[1,1,1,1]]
piece_i5 = [[1,1,1,1,1]]

# Moderate Pieces
piece_v3 = [[1,0],
           [1,1]]
piece_o4 = [[1,1],
           [1,1]]
piece_z4 = [[0,1,1],
           [1,1,0]]
piece_t4 = [[0,1,0],
           [1,1,1]]
piece_l4 = [[1,0,0],
           [1,1,1]]
piece_u = [[1,0,1],
           [1,1,1]]
piece_p = [[1,1,0],
           [1,1,1]]

# Complex Pieces
piece_y = [[0,1,0,0],
           [1,1,1,1]]
piece_l5 = [[1,0,0,0],
           [1,1,1,1]]
piece_n = [[1,1,0,0],
           [0,1,1,1]]
piece_x = [[0,1,0],
           [1,1,1],
           [0,1,0]]
piece_w = [[0,0,1],
           [0,1,1],
           [1,1,0]]
piece_f = [[1,1,0],
           [0,1,1],
           [0,1,0]]
piece_z5 = [[1,1,0],
           [0,1,0],
           [0,1,1]]
piece_t = [[1,1,1],
           [0,1,0],
           [0,1,0]]
piece_v5 = [[1,0,0],
           [1,0,0],
           [1,1,1]]