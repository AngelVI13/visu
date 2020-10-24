import os
import pygame
from typing import Tuple
from models.square import Square, Color


class Tile:
    TILE_SIZE = 64

    # Load and rescale images
    WHITE_TILE = pygame.image.load(os.path.abspath('../media/white_tile.png'))
    WHITE_TILE = pygame.transform.scale(WHITE_TILE, (TILE_SIZE, TILE_SIZE))
    BLACK_TILE = pygame.image.load(os.path.abspath('../media/purple_tile.png'))
    BLACK_TILE = pygame.transform.scale(BLACK_TILE, (TILE_SIZE, TILE_SIZE))

    def __init__(self, square: Square):
        self.square = square
        self.img = self.WHITE_TILE if square.color == Color.WHITE else self.BLACK_TILE

    def render(self, screen: pygame.Surface, offsets: Tuple[int, int]):
        offset_x, offset_y = offsets

        # flip a1 tile to be at the bottom of the screen
        # otherwise a1 (file==0, rank==0) will be drawn in the top left corner
        # NOTE: files go from 0-7 inclusive. Thats why we do 7 - file.
        tile_x = (7 - self.square.file) * self.TILE_SIZE
        tile_y = self.square.rank*self.TILE_SIZE
        screen.blit(self.img, (tile_x + offset_x, tile_y + offset_y))