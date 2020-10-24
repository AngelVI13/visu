import time
from abc import ABC, abstractmethod
from typing import List
from operator import xor
from functools import partial, reduce
from itertools import cycle, chain
from models.square import Square


class Board:
    def __init__(self):
        # holds information of all pieces on the board an their locations
        self.pieces = []

    @property
    def occupied(self) -> List[Square]:
        """Get list of occupied squares."""
        return [piece.square for piece in self.pieces]

    def get_singular_squares(self) -> List[Square]:
        """Return the list of squares to which only 1 piece can go."""
        all_moves = [set(piece.get_moves()) for piece in self.pieces]
        # set(a) ^ set(b) = non-intersecting elements from a and b
        return list(reduce(xor, all_moves))
