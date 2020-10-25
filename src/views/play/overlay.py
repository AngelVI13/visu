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
    objects: Dict[str, Any]


class Overlay:
    def __init__(
            self, 
            screen: pygame.Surface, 
            rect: pygame.Rect, 
            color: Tuple[int, int, int], 
            opacity: int,
            padding: int = 10
        ):
        self.screen = screen # opacity, color, font_color

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.rect = rect
        self.color = color
        self.opacity = opacity
        self.elements = []
        self.padding = padding

    def add_element(self, type: ElementType, **options):
        if type == ElementType.TEXT:
            text_element = self._create_text_element(**options)
            self.elements.append(Element(type, text_element))

    def _create_text_element(self, **options):
        return create_message(pos=self.rect.topleft, **options)

    def render(self):
        # compute the size of the overlay based on the text size
        pygame.draw.rect(self.screen, self.color, self.rect, width=8, border_radius=8)

        # per-pixel alpha
        surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # notice the alpha value in the color
        surface.fill((*self.color, self.opacity))

        # center_x, center_y = text_rect.x, text_rect.y
        self.screen.blit(surface, self.rect.topleft)

        offset_x, offset_y = self.rect.topleft
        offset_x += self.padding  # x padding is applied just once
        
        for element in self.elements:
            # apply vertical padding between every element
            offset_y += self.padding

            if element.type == ElementType.TEXT:
                surface, rect = element.objects
                # update every text element's position
                rect.topleft = offset_x, offset_y
                self.screen.blit(surface, rect)

                # update height for next element
                offset_y += rect.h