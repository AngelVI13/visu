import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join("..", "src")))

from pytest import raises
from models.board import Board
from models.square import Square
from models.pieces import Bishop, Knight


def test_get_singular_squares():
    board = Board()

    bishop = Bishop(Square.from_notation("a1"), board)
    knight = Knight(Square.from_notation("b1"), board)

    board.add_piece(bishop)
    board.add_piece(knight)

    squares = board.get_singular_squares()
    assert isinstance(squares, list)
    assert all(isinstance(square, Square) for square in squares)
    assert len(squares) == 8
    assert Square.from_notation("b2") in squares
    assert Square.from_notation("h8") in squares
    assert Square.from_notation("c3") not in squares
    assert Square.from_notation("a3") in squares
    assert Square.from_notation("d2") in squares


def test_get_piece_that_reaches_square():
    board = Board()

    bishop = Bishop(Square.from_notation("a1"), board)
    knight = Knight(Square.from_notation("b1"), board)

    board.add_piece(bishop)
    board.add_piece(knight)

    square = Square.from_notation("a3")
    assert isinstance(board.get_piece_that_reaches_square(square), Knight)
    
    square = Square.from_notation("b2")
    assert isinstance(board.get_piece_that_reaches_square(square), Bishop)

    with raises(ValueError):
        square = Square.from_notation("e2")
        _ = board.get_piece_that_reaches_square(square)
