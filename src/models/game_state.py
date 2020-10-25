from enum import Enum, auto
from models.board import Board
from models.pieces import Bishop, Knight, Rook, Queen, King, Piece
from models.square import Square
from random import choice


class States(Enum):
    PRE_GAME = auto()
    PLAY = auto()
    GAME_OVER = auto()


class GameState:
    MAX_LEVEL = 5
    # for every level add the corresponding piece to the board
    LEVELS = {
        1: Bishop,
        2: Knight,
        3: Rook,
        4: King,
        5: Queen
    }

    def __init__(self, board: Board):
        self.board = board
        self.current_state = States.PRE_GAME
        self.level = 0
        self.score = 0

    def setup_pre_game(self):
        """Reset board and set 2 initial pieces"""

        # reset game info
        self.current_state = States.PRE_GAME
        self.level = 0
        self.board.reset()

        # add initial 2 pieces to the board (knight & bishop)
        all_squares = list(range(64))

        for piece in (Bishop, Knight):
            square = choice(all_squares)
            all_squares.remove(square)
            piece_object = piece(Square.from_index(square), self.board)
            self.board.add_piece(piece_object)

    def update_game(self, guessed_piece: Piece):
        pass