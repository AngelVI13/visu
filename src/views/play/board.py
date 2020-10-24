import pygame

import models.board as model
from models.square import Square
from views.play.defines import *
from views.helpers import message_display
from views.play.tile import Tile
from views.play.pieces import Pieces
from settings.color_scheme import *
from settings.display import DISPLAY_SCALING


class Board:
    def __init__(self, screen: pygame.Surface, board_model: model.Board):
        self.screen = screen
        self.board_model = board_model

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.board_offset_x = (self.screen_width - 8 * Tile.TILE_SIZE) // 2
        self.board_offset_y = (self.screen_height - 8 * Tile.TILE_SIZE) // 2

        # Create board tiles
        self.tiles = []
        for file in range(8):
            for rank in range(8):
                tile = Tile(Square(file, rank))
                self.tiles.append(tile)

    def render(self):
        self.screen.fill(WHITE)
        
        for tile in self.tiles:
            piece_img = None
            piece_at_square = self.board_model.get_piece_at_square(tile.square)
            if piece_at_square:
                piece_img = Pieces.get_image(piece_at_square)

            tile.render(self.screen, (self.board_offset_x, self.board_offset_y), piece_img)

        message_display(surface=self.screen, text="Test", pos=(self.screen_width / 2, self.screen_height / 3),
            font='comicsansms', size=40)
