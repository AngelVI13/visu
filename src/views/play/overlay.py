import pygame
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Tuple, NamedTuple, Dict, Any, Callable

from models.game_state import GameState
from views.play.defines import *
from views.common.button import Button
from views.play.board import Board
from views.helpers import get_text_objects
from settings.color_scheme import *
from settings.display import DISPLAY_SCALING


class ElementTypes(Enum):
    TEXT = auto()
    BUTTON = auto()


class BaseElement(ABC):
    @abstractmethod
    def blit(self, surface, *args, **kwargs) -> pygame.Surface:
        pass


class TextElement(BaseElement):
    def __init__(self, text: str, font: pygame.font.Font, color: pygame.Color):
        self.text = text
        self.font = font
        self.color = color

    def blit(self, surface, pos) -> pygame.Surface:
        """Method that blits multiline text on a provided surface"""

        # 2D array where each row is a list of words.
        words = [word.split(' ') for word in self.text.splitlines()]
        space_width, *_ = self.font.size(' ')  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = self.font.render(word, True, self.color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x, *_ = pos  # Reset the x.
                    y += word_height  # Start on new row.

                surface.blit(word_surface, (x, y))
                x += word_width + space_width
            x, *_ = pos  # Reset the x.
            y += word_height  # Start on new row.
        return surface


class ButtonElement(BaseElement):
    def __init__(
        self,
        text: str,
        color: pygame.Color,
        accent_color: pygame.Color,
        action: Callable,
        font: pygame.font.Font,
        font_color: pygame.Color,
    ):
        self.text = text
        self.color = color
        self.accent_color = accent_color
        self.action = action
        self.font = font
        self.font_color = font_color

        # create text objects
        self.text_surf, self.text_rect = get_text_objects(
            self.text, self.font, color=self.font_color
        )

    def blit(self, surface: pygame.Surface, rect: pygame.Rect, mouse: Tuple[int, int]) -> pygame.Surface:
        x, y = rect.topleft
        w, h = rect.size
        self.text_rect.center = x + (w / 2), y + (h / 2)

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(surface, self.accent_color, rect)
        else:
            pygame.draw.rect(surface, self.color, rect)

        surface.blit(self.text_surf, self.text_rect)
        return surface


# todo add support for horizontal elements
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
        self.elements = {}
        self.padding = padding
        self.font = font

    def add_element(self, type: ElementTypes, proportion: float, **kwargs):
        if type == ElementTypes.TEXT:
            element = self._create_text_element(**kwargs)
        elif type == ElementTypes.BUTTON:
            element = self._create_button_element(**kwargs)

        self.elements[element] = proportion

    def _create_text_element(self, text: str, size: int, color: pygame.Color):
        font_object = pygame.font.SysFont(self.font, size * DISPLAY_SCALING)
        return TextElement(text, font_object, color)

    def _create_button_element(
            self,
            text: str,
            color: pygame.Color,
            accent_color: pygame.Color,
            action: Callable,
            font_size: int,
            font_color: pygame.Color,
        ):
        font_object = pygame.font.SysFont(self.font, font_size * DISPLAY_SCALING)
        return ButtonElement(text, color, accent_color, action, font_object, font_color)

    def render(self, mouse_pos: Tuple[int, int]):
        # compute the size of the overlay based on the text size
        pygame.draw.rect(
            self.screen, self.color, self.rect,
            # border_radius=8
        )

        offset_x, offset_y = self.rect.topleft
        offset_x += self.padding  # x padding is applied just once

        # todo add check that propotions add to 1
        for element, proportion in self.elements.items():
            # apply vertical padding between every element
            offset_y += self.padding

            # create element surface
            surface = pygame.Surface(
                (self.rect.w - 2*self.padding, # width
                    (self.rect.h * proportion) - 1.5*self.padding), # height
                pygame.HWSURFACE
            )
            surface.fill((*self.color, 255))

            if isinstance(element, TextElement):
                # position relative to the new surface
                surface = element.blit(surface, pos=(0, 0))
            elif isinstance(element, ButtonElement):
                mouse_x, mouse_y = mouse_pos
                mouse_x -= offset_x
                mouse_y -= offset_y

                surface = element.blit(
                    surface,
                    pygame.Rect(0, 0, surface.get_width(), surface.get_height()),
                    mouse=(mouse_x, mouse_y)
                )

            # blit element surface on the screen & update height for next element
            self.screen.blit(surface, (offset_x, offset_y))
            offset_y += surface.get_height()
