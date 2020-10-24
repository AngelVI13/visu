import time
from abc import ABC, abstractmethod
from typing import List
from functools import partial
from itertools import cycle, chain


class Board:
    def __init__(self):
        # create empty 8x8 matrix to hold the board information
        self.position = [[None] * 8 for _ in range(8)]
        # holds information of all pieces on the board an their locations
        self.pieces = []

    @property
    def occupied(self):
        return [piece.square for piece in self.pieces]
