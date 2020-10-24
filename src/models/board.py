import time
from abc import ABC, abstractmethod
from typing import List, Optional
from operator import xor
from functools import partial, reduce
from itertools import cycle, chain
from models.square import Square
from models.pieces import Piece


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

    def get_piece_that_reaches_square(self, square: Square) -> Piece:
        """Get piece object that can reach the given square."""
        for piece in self.pieces:
            if square in piece.get_moves():
                return piece

        raise ValueError(f"No piece can reach square: {square}")

    def get_piece_at_square(self, square: Square) -> Optional[Piece]:
        """Get piece object at the give square. If no piece is on
        this suqare return None"""
        for piece in self.pieces:
            if square == piece.square:
                return piece
        return None
