import pygame

import models.board as model
from views.play.defines import *
from views.helpers import message_display
from views.play.board import Board
from settings.color_scheme import *
from settings.display import DISPLAY_SCALING


class Game:
    def __init__(self, screen: pygame.Surface, board_model: model.Board):
        self.screen = screen
        self.board_model = board_model

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.board_view = Board(self.screen, self.board_model)

    def render(self):
        self.board_view.render()