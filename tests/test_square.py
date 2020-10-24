import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join("..", "src")))

from pytest import raises
from models.square import Square, Color


def test_square_notation():
    square = Square(file=0, rank=0)
    assert square.notation == "a1"

    square = Square(file=7, rank=7)
    assert square.notation == "h8"

    with raises(ValueError):
        _ = Square(file=10, rank=10)

    with raises(ValueError):
        _ = Square(file=-1, rank=-1)

    with raises(ValueError):
        _ = Square(file=8, rank=8)


def test_square_color():
    squares = [
        # black squares
        ({"file": 0, "rank": 0}, Color.BLACK),
        ({"file": 7, "rank": 7}, Color.BLACK),
        ({"file": 2, "rank": 0}, Color.BLACK),
        ({"file": 3, "rank": 1}, Color.BLACK),
        ({"file": 5, "rank": 5}, Color.BLACK),
        ({"file": 4, "rank": 4}, Color.BLACK),

        # white squares
        ({"file": 1, "rank": 0}, Color.WHITE),
        ({"file": 0, "rank": 7}, Color.WHITE),
        ({"file": 2, "rank": 1}, Color.WHITE),
        ({"file": 3, "rank": 2}, Color.WHITE),
        ({"file": 7, "rank": 0}, Color.WHITE),
        ({"file": 3, "rank": 4}, Color.WHITE),
    ]

    for position, expected_color in squares:
        square = Square(**position)
        assert square.color == expected_color


def test_square_from_notation():
    square = Square.from_notation("a1")
    assert isinstance(square, Square)
    assert square.file == 0
    assert square.rank == 0

    square = Square.from_notation("d4")
    assert square.file == 3
    assert square.rank == 3

    square = Square.from_notation("h7")
    assert square.file == 7
    assert square.rank == 6

    with raises(TypeError):
        _ = Square.from_notation(5)

    with raises(ValueError):
        _ = Square.from_notation("a12")
    
    with raises(ValueError):
        _ = Square.from_notation("z1")
    
    with raises(ValueError):
        _ = Square.from_notation("aa")
