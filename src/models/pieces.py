from abc import ABC, abstractmethod
from typing import NamedTuple, List
from models.square import Square


class DirectionVec(NamedTuple):
    file: int
    rank: int


class Directions:
    ORTHOGONAL = {
        'North': DirectionVec(0,-1),
        'South': DirectionVec(0,1),
        'West': DirectionVec(-1,0),
        'East': DirectionVec(1,0),
    }
    
    DIAGONAL = {
        'Topleft': DirectionVec(-1,-1),
        'Topright': DirectionVec(-1,1),
        'Bottomleft': DirectionVec(1,-1),
        'Bottomright': DirectionVec(1,1),
    }
    
    COMBINED = {**ORTHOGONAL, **DIAGONAL}
    
    KNIGHT = {
        'TL': DirectionVec(-1,-2),
        'TL2': DirectionVec(-2,-1),
        'BL': DirectionVec(-2,1),
        'BL2': DirectionVec(-1,2),
        'TR': DirectionVec(1,-2),
        'TR2': DirectionVec(2,-1),
        'BR': DirectionVec(2,1),
        'BR2': DirectionVec(1,2),
    }
    

PIECE_ABBREVIATIONS = list(iter("BRQKN"))


class Piece(ABC):
    directions = None
    abbreviation = None

    def __init__(self, square: Square, board):
        self.square = square
        self.board = board  # reference to board object

    @abstractmethod
    def get_moves(self) -> List[Square]:
        pass


class SlidingPiece(Piece):
    def get_moves(self) -> List[Square]:
        moves = []

        for direction in self.directions.values():
            new_square = self.square # start from current square

            while True:
                new_file = new_square.file + direction.file
                new_rank = new_square.rank + direction.rank

                try:
                    new_square = Square(new_file, new_rank)
                except ValueError:
                    # we are out of bounds -> this square doesn't exist
                    # move to next direction
                    break

                # if square exists but its occupied -> move to next direction
                if new_square in self.board.occupied:
                    break

                moves.append(new_square)

        return moves


class NonSlidingPiece(Piece):
    def get_moves(self) -> List[Square]:
        moves = []

        for direction in self.directions.values():
            new_file = self.square.file + direction.file
            new_rank = self.square.rank + direction.rank

            try:
                new_square = Square(new_file, new_rank)
            except ValueError:
                # we are out of bounds -> this square doesn't exist
                # move to next direction
                continue

            # if square exists but its occupied -> move to next direction
            if new_square in self.board.occupied:
                continue

            moves.append(new_square)

        return moves


class Bishop(SlidingPiece):
    directions = Directions.DIAGONAL
    abbreviation = "B"


class Rook(SlidingPiece):
    directions = Directions.ORTHOGONAL
    abbreviation = "R"
    

class Queen(SlidingPiece):
    directions = Directions.COMBINED
    abbreviation = "Q"


class King(NonSlidingPiece):
    directions = Directions.COMBINED
    abbreviation = "K"


class Knight(NonSlidingPiece):
    directions = Directions.KNIGHT
    abbreviation = "N"
