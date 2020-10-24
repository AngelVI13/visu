import os
import pygame
from typing import Tuple
from models.square import Color
from models.pieces import Bishop, Rook, Queen, King, Knight, Piece


class Pieces:
    PIECE_SIZE = 64

    # Load and rescale images
    KNIGHT_W = pygame.image.load(os.path.abspath('../media/knight_w.png'))
    KNIGHT_B = pygame.image.load(os.path.abspath('../media/knight_b.png'))
    BISHOP_W = pygame.image.load(os.path.abspath('../media/bishop_w.png'))
    BISHOP_B = pygame.image.load(os.path.abspath('../media/bishop_b.png'))
    ROOK_W = pygame.image.load(os.path.abspath('../media/rook_w.png'))
    ROOK_B = pygame.image.load(os.path.abspath('../media/rook_b.png'))
    QUEEN_W = pygame.image.load(os.path.abspath('../media/queen_w.png'))
    QUEEN_B = pygame.image.load(os.path.abspath('../media/queen_b.png'))
    KING_W = pygame.image.load(os.path.abspath('../media/king_w.png'))
    KING_B = pygame.image.load(os.path.abspath('../media/king_b.png'))
    
    KNIGHT_W = pygame.transform.scale(KNIGHT_W, (PIECE_SIZE, PIECE_SIZE))
    KNIGHT_B = pygame.transform.scale(KNIGHT_B, (PIECE_SIZE, PIECE_SIZE))
    BISHOP_W = pygame.transform.scale(BISHOP_W, (PIECE_SIZE, PIECE_SIZE))
    BISHOP_B = pygame.transform.scale(BISHOP_B, (PIECE_SIZE, PIECE_SIZE))
    ROOK_W = pygame.transform.scale(ROOK_W, (PIECE_SIZE, PIECE_SIZE))
    ROOK_B = pygame.transform.scale(ROOK_B, (PIECE_SIZE, PIECE_SIZE))
    QUEEN_W = pygame.transform.scale(QUEEN_W, (PIECE_SIZE, PIECE_SIZE))
    QUEEN_B = pygame.transform.scale(QUEEN_B, (PIECE_SIZE, PIECE_SIZE))
    KING_W = pygame.transform.scale(KING_W, (PIECE_SIZE, PIECE_SIZE))
    KING_B = pygame.transform.scale(KING_B, (PIECE_SIZE, PIECE_SIZE))
    
    @classmethod
    def get_image(cls, piece: Piece):
        if isinstance(piece, Bishop):
            return cls.BISHOP_W if piece.square.color == Color.WHITE else cls.BISHOP_B
        elif isinstance(piece, Knight):
            return cls.KNIGHT_W if piece.square.color == Color.WHITE else cls.KNIGHT_B
        elif isinstance(piece, Rook):
            return cls.ROOK_W if piece.square.color == Color.WHITE else cls.ROOK_B
        elif isinstance(piece, Queen):
            return cls.QUEEN_W if piece.square.color == Color.WHITE else cls.QUEEN_B
        elif isinstance(piece, King):
            return cls.KING_W if piece.square.color == Color.WHITE else cls.KING_B
        else:
            raise ValueError(f"Unsupported piece: {type(piece)}")
        