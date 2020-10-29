import pygame

from event import MouseEventMove
from models.game_state import GameState
from views.play.defines import *
from views.helpers import create_message
from views.base_view import BaseView
from views.play.board import Board
from views.play.overlay import Overlay, ButtonElement, TextElement, ElementTypes
from settings.color_scheme import *
from settings.display import DISPLAY_SCALING


class Game(BaseView):
    def __init__(self, screen: pygame.Surface, game_model: GameState):
        self.screen = screen
        self.game_model = game_model

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.board_view = Board(self.screen, self.game_model)

        self.overlay = Overlay(
            self.screen,
            rect=pygame.Rect(self.screen_width / 4, self.screen_height / 4, self.screen_width / 2, self.screen_height / 2),
            color=WHITE_1,
            opacity=220,
            font='comicsansms',
        )
        self.overlay.add_element(
            ElementTypes.TEXT,
            proportion=0.20,
            text="Visualization Training",
            size=26,
            color=BLACK
        )
        self.overlay.add_element(
            ElementTypes.TEXT,
            proportion=0.60,
            text=(
                "The aim of the game: Say which piece can "
                "reach a given square. You start with 2 pieces "
                "and get 1 more for every 10 right answers.\n\n"
                "The catch: you cannot see where your pieces are!\n"
            ),
            size=16,
            color=BLACK
        )
        self.overlay.add_element(
            ElementTypes.BUTTON,
            proportion=0.20,
            text="Start",
            color=PURPLE,
            accent_color=PURPLE_HIGHLIGHT,
            action=None,
            font_size=26,
            font_color=BLACK,
        )

        self.input_ = None

    def register_inputs(self, input_):
        self.input_ = input_

    def render(self):
        self.screen.fill(WHITE)

        self.board_view.render()

        mouse_position = self.input_.pos if isinstance(self.input_, MouseEventMove) else [0, 0]
        self.overlay.render(mouse_position)

        # create_message(surface=self.screen, text="Test", pos=(self.screen_width / 2, self.screen_height / 3),
        #     font='comicsansms', size=40)