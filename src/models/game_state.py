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
    QUESTIONS_PER_LEVEL = 5
    MAX_LEVEL = 5
    # for every level add the corresponding piece to the board
    LEVELS = {
        1: Bishop,
        2: Knight,
        3: Rook,
        4: King,
        5: Queen
    }

    def __init__(self):
        self.board = Board()
        self.current_state = States.PRE_GAME
        self.level = 0
        self.score = 0

    def setup_pre_game(self):
        """Reset board and set 2 initial pieces"""

        # reset game info
        self.current_state = States.PLAY
        self.level = 0
        self.board.reset()

        # add initial 2 pieces to the board (knight & bishop)
        all_squares = list(range(64))

        for piece in (Bishop, Knight):
            square = choice(all_squares)
            all_squares.remove(square)
            piece_object = piece(Square.from_index(square), self.board)
            self.board.add_piece(piece_object)

    def print_piece_info(self):
        for piece in self.board.pieces:
            print(f"You have a {piece.__class__.__name__} on {piece.square.notation}")

    def generate_new_square(self):
        return choice(self.board.get_singular_squares())

    def generate_new_piece(self, level: int) -> Piece:
        all_squares = list(range(64))
        for piece in self.board.pieces:
            all_squares.remove(piece.square.index)

        square_index = choice(all_squares)
        square = Square.from_index(square_index)

        new_piece_class = self.LEVELS.get(level)
        new_piece = new_piece_class(square, self.board)
        return new_piece

    def update_game(self, guessed_piece: Piece, new_square: Square):
        self.score += 1

        # change position of the piece
        for piece in self.board.pieces:
            if piece is guessed_piece:
                piece.square = new_square

        new_level = self.score // self.QUESTIONS_PER_LEVEL
        if new_level > self.level:
            self.level = new_level

            print(f"------------------")
            print(f"---> LEVEL UP <---")
            print(f"------------------")

            new_piece = self.generate_new_piece(self.level)
            self.board.add_piece(new_piece)
            print(f"You got a NEW {new_piece.__class__.__name__} on {new_piece.square.notation}")
