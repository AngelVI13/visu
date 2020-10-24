import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join("..", "src")))

from pytest import raises
from models.pieces import Bishop, Rook, Queen, King, Knight
from models.board import Board
from models.square import Square


def test_bishop_moves():
    board = Board()

    # Check move generation when bishop is on A1
    bishop = Bishop(Square.from_notation("a1"), board)

    moves = bishop.get_moves()
    assert len(moves) == 7
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=1, rank=1) in moves
    assert Square(file=7, rank=7) in moves

    # Check move generation when bishop is on D4
    bishop = Bishop(Square.from_notation("d4"), board)

    moves = bishop.get_moves()
    assert len(moves) == 13
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=1, rank=1) in moves
    assert Square(file=7, rank=7) in moves
    assert Square(file=0, rank=6) in moves
    assert Square(file=6, rank=0) in moves

    # Check move generation when bishop is on E4
    # and there is a blockin piece on F5
    bishop = Bishop(Square.from_notation("e4"), board)
    blocking_bishop = Bishop(Square.from_notation("f5"), board)
    
    board.pieces.append(blocking_bishop)

    moves = bishop.get_moves()
    assert len(moves) == 10
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=1, rank=0) in moves
    assert Square(file=7, rank=0) in moves
    assert Square(file=0, rank=7) in moves
    assert Square(file=7, rank=6) not in moves

def test_rook_moves():
    board = Board()

    # Check move generation when rook is on A1
    rook = Rook(Square.from_notation("a1"), board)

    moves = rook.get_moves()
    assert len(moves) == 14
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=7, rank=0) in moves
    assert Square(file=0, rank=7) in moves

    # Check move generation when rook is on D4
    rook = Rook(Square.from_notation("d4"), board)

    moves = rook.get_moves()
    assert len(moves) == 14
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=0, rank=3) in moves
    assert Square(file=7, rank=3) in moves
    assert Square(file=3, rank=7) in moves
    assert Square(file=3, rank=0) in moves

    # Check move generation when rook is on D4
    # and there is a blockin piece on F4
    rook = Rook(Square.from_notation("d4"), board)
    blocking_bishop = Bishop(Square.from_notation("f4"), board)
    
    board.pieces.append(blocking_bishop)

    moves = rook.get_moves()
    assert len(moves) == 11
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=0, rank=3) in moves
    assert Square(file=4, rank=3) in moves
    assert Square(file=3, rank=0) in moves
    assert Square(file=3, rank=7) in moves
    assert Square(file=5, rank=3) not in moves

def test_queen_moves():
    board = Board()

    # Check move generation when queen is on A1
    queen = Queen(Square.from_notation("a1"), board)

    moves = queen.get_moves()
    assert len(moves) == 21
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=7, rank=0) in moves
    assert Square(file=0, rank=7) in moves
    assert Square(file=7, rank=7) in moves

    # Check move generation when queen is on D4
    queen = Queen(Square.from_notation("d4"), board)

    moves = queen.get_moves()
    assert len(moves) == 27
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=0, rank=3) in moves
    assert Square(file=7, rank=3) in moves
    assert Square(file=3, rank=7) in moves
    assert Square(file=3, rank=0) in moves
    assert Square(file=1, rank=1) in moves
    assert Square(file=7, rank=7) in moves
    assert Square(file=0, rank=6) in moves
    assert Square(file=6, rank=0) in moves

    # Check move generation when queen is on D4
    # and there is a blockin piece on F4
    queen = Queen(Square.from_notation("d4"), board)
    blocking_bishop1 = Bishop(Square.from_notation("c4"), board)
    blocking_bishop2 = Bishop(Square.from_notation("c3"), board)
    
    board.pieces.append(blocking_bishop1)
    board.pieces.append(blocking_bishop2)

    moves = queen.get_moves()
    assert len(moves) == 21
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=7, rank=3) in moves
    assert Square(file=4, rank=3) in moves
    assert Square(file=3, rank=0) in moves
    assert Square(file=3, rank=7) in moves
    assert Square(file=5, rank=3) in moves
    assert Square(file=1, rank=5) in moves
    assert Square(file=6, rank=0) in moves
    assert Square(file=0, rank=6) in moves
    assert Square(file=0, rank=0) not in moves
    assert Square(file=0, rank=3) not in moves


def test_knight_moves():
    board = Board()

    # Check move generation when knight is on A1
    knight = Knight(Square.from_notation("a1"), board)

    moves = knight.get_moves()
    assert len(moves) == 2
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=1, rank=2) in moves
    assert Square(file=2, rank=1) in moves

    # Check move generation when knight is on D4
    knight = Knight(Square.from_notation("d4"), board)

    moves = knight.get_moves()
    assert len(moves) == 8
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=1, rank=2) in moves
    assert Square(file=1, rank=4) in moves
    assert Square(file=2, rank=5) in moves
    assert Square(file=2, rank=1) in moves
    assert Square(file=4, rank=1) in moves
    assert Square(file=4, rank=5) in moves
    assert Square(file=5, rank=4) in moves
    assert Square(file=5, rank=2) in moves

    # Check move generation when knight is on D4
    # and there is a blockin piece on C2
    knight = Knight(Square.from_notation("d4"), board)
    blocking_bishop = Bishop(Square.from_notation("c2"), board)
    
    board.pieces.append(blocking_bishop)

    moves = knight.get_moves()
    assert len(moves) == 7
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=1, rank=2) in moves
    assert Square(file=1, rank=4) in moves
    assert Square(file=2, rank=5) in moves
    assert Square(file=2, rank=1) not in moves
    assert Square(file=4, rank=1) in moves
    assert Square(file=4, rank=5) in moves
    assert Square(file=5, rank=4) in moves
    assert Square(file=5, rank=2) in moves


def test_king_moves():
    board = Board()

    # Check move generation when king is on A1
    king = King(Square.from_notation("a1"), board)

    moves = king.get_moves()
    assert len(moves) == 3
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=0, rank=1) in moves
    assert Square(file=1, rank=1) in moves
    assert Square(file=1, rank=0) in moves

    # Check move generation when king is on D4
    king = King(Square.from_notation("d4"), board)

    moves = king.get_moves()
    assert len(moves) == 8
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=2, rank=2) in moves
    assert Square(file=2, rank=3) in moves
    assert Square(file=2, rank=4) in moves
    assert Square(file=3, rank=2) in moves
    assert Square(file=3, rank=4) in moves
    assert Square(file=4, rank=2) in moves
    assert Square(file=4, rank=3) in moves
    assert Square(file=4, rank=4) in moves

    # Check move generation when king is on D4
    # and there is a blockin piece on C5
    king = King(Square.from_notation("d4"), board)
    blocking_bishop = Bishop(Square.from_notation("c5"), board)
    
    board.pieces.append(blocking_bishop)

    moves = king.get_moves()
    assert len(moves) == 7
    assert all(isinstance(move, Square) for move in moves)
    assert Square(file=2, rank=2) in moves
    assert Square(file=2, rank=3) in moves
    assert Square(file=2, rank=4) not in moves
    assert Square(file=3, rank=2) in moves
    assert Square(file=3, rank=4) in moves
    assert Square(file=4, rank=2) in moves
    assert Square(file=4, rank=3) in moves
    assert Square(file=4, rank=4) in moves
