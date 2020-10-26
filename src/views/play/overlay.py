import pygame

from models.game_state import GameState
from views.play.defines import *
from views.helpers import create_message
from views.play.board import Board
from settings.color_scheme import *
from settings.display import DISPLAY_SCALING
from typing import Tuple, NamedTuple, Dict, Any
from enum import Enum, auto


class ElementType(Enum):
    TEXT = auto()
    BUTTON = auto()


class Element(NamedTuple):
    type: ElementType
    proportion: float
    options: Dict[str, Any]


class Overlay:
    def __init__(
            self,
            screen: pygame.Surface,
            rect: pygame.Rect,
            color: Tuple[int, int, int],
            opacity: int,
            padding: int = 10,
            font: str = "comicsansms"
        ):
        self.screen = screen # opacity, color, font_color

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.rect = rect
        self.color = color
        self.opacity = opacity
        self.elements = []
        self.padding = padding
        self.font = font

    def add_element(self, type: ElementType, proportion: float, **options):
        if type == ElementType.TEXT:
            self.elements.append(Element(type, proportion, options))

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        """Method that blits multiline text on a provided surface"""

        # 2D array where each row is a list of words.
        words = [word.split(' ') for word in text.splitlines()]
        space_width, *_ = font.size(' ')  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x, *_ = pos  # Reset the x.
                    y += word_height  # Start on new row.

                surface.blit(word_surface, (x, y))
                x += word_width + space_width
            x, *_ = pos  # Reset the x.
            y += word_height  # Start on new row.
        return surface

    def render(self):
        # compute the size of the overlay based on the text size
        pygame.draw.rect(
            self.screen, self.color, self.rect,
            # border_radius=8
        )

        offset_x, offset_y = self.rect.topleft
        offset_x += self.padding  # x padding is applied just once

        for element in self.elements:
            # apply vertical padding between every element
            offset_y += self.padding

            # create element surface
            surface = pygame.Surface(
                (self.rect.w - self.padding, (self.rect.h * element.proportion) - self.padding),
                pygame.HWSURFACE
            )
            surface.fill((*self.color, 255))

            if element.type == ElementType.TEXT:
                surface = self.blit_text(
                    surface,
                    text=element.options["text"],
                    pos=(0, 0),  # position relative to the new surface
                    font=pygame.font.SysFont(self.font, element.options["size"] * DISPLAY_SCALING),
                    color=element.options["color"],
                )
                self.screen.blit(surface, (offset_x, offset_y))
                # update height for next element
                offset_y += surface.get_height()

            elif element.type == ElementType.BUTTON:
                pass
