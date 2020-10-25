import pygame

from models.game_state import GameState, States
from models.square import Square
from views.play.defines import *
from views.play.tile import Tile
from views.play.pieces import Pieces
from settings.color_scheme import *
from settings.display import DISPLAY_SCALING


class Board:
    def __init__(self, screen: pygame.Surface, game_model: GameState):
        self.screen = screen
        self.game_model = game_model

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
        for tile in self.tiles:
            piece_img = None
            piece_at_square = self.game_model.board.get_piece_at_square(tile.square)

            # show pieces only if we are in pre-game state or when the game is over
            if piece_at_square and self.game_model.current_state != States.PLAY:
                piece_img = Pieces.get_image(piece_at_square)

            tile.render(self.screen, (self.board_offset_x, self.board_offset_y), piece_img)
