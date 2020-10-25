import pygame

from models.game_state import GameState
from views.play.defines import *
from views.helpers import message_display
from views.play.board import Board
from settings.color_scheme import *
from settings.display import DISPLAY_SCALING


class Game:
    def __init__(self, screen: pygame.Surface, game_model: GameState):
        self.screen = screen
        self.game_model = game_model

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.board_view = Board(self.screen, self.game_model)

    def render(self):
        self.screen.fill(WHITE)
        
        self.board_view.render()

        message_display(surface=self.screen, text="Test", pos=(self.screen_width / 2, self.screen_height / 3),
            font='comicsansms', size=40)