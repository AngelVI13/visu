import pygame
from enum import Enum, auto

from event import MouseEventMove
from settings.display import DISPLAY_SCALING
from settings.color_scheme import PURPLE, PURPLE_HIGHLIGHT
from views.menu.background import Background
from views.helpers import create_message
from views.common import Button
from views.base_view import BaseView


class MenuActions(Enum):
    PLAY = auto()
    SETTINGS = auto()
    HELP = auto()
    QUIT = auto()


class Menu(BaseView):
    HEADING = "Visu"
    # todo decide how to nicely handle these values
    # Menu buttons
    BUTTON_ACTIONS = {
        "Play": MenuActions.PLAY, 
        "Settings": MenuActions.SETTINGS, 
        "Help": MenuActions.HELP, 
        "Quit": MenuActions.QUIT
    }
    
    # menu button properties
    _BUTTON_WIDTH = 300 * DISPLAY_SCALING
    _BUTTON_HEIGHT = 50 * DISPLAY_SCALING
    _BUTTON_Y_SPACING = 1.5
    _BUTTON_X_SPACING = 0.5

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.background = Background(screen)

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        # Compute locations of buttons & add predefined common colors
        self.COMMON_BUTTON_PROPERTIES = {
            "x": (self.screen_width - self._BUTTON_WIDTH) / 2,
            'w': self._BUTTON_WIDTH, 'h': self._BUTTON_HEIGHT, 'ic': PURPLE, 'ac': PURPLE_HIGHLIGHT, 
        }

        self.MENU_BUTTON_PROPERTIES = [  # todo add names instead of integers as keys
            {"y": (self.screen_height/3) + (i + 1) * self._BUTTON_HEIGHT * self._BUTTON_Y_SPACING } 
            for i in range(len(self.BUTTON_ACTIONS))
        ]

        self.buttons = []

        button_action_tuples = list(self.BUTTON_ACTIONS.items())
        # create button object with common & calculated button properties
        for idx, button_properties in enumerate(self.MENU_BUTTON_PROPERTIES):
            button_properties.update(self.COMMON_BUTTON_PROPERTIES)

            msg, action = button_action_tuples[idx]
            self.buttons.append(
                Button(msg=msg, action=action, **self.MENU_BUTTON_PROPERTIES[idx])
            )

        # holds input events (mouse/keyboard)
        self.input_ = None

    def register_inputs(self, input_):
        self.input_ = input_

    def render(self):
        self.screen.fill(pygame.Color("white"))

        self.background.update()

        text_surf, text_rect = create_message(
            text=self.HEADING, pos=(self.screen.get_width() / 2, self.screen.get_height() / 3),
            font='comicsansms', size=40
        )
        self.screen.blit(text_surf, text_rect)

        # only ask for mouse status once and not for every button
        mouse = self.input_.pos if isinstance(self.input_, MouseEventMove) else [0, 0]
        
        for button in self.buttons:
            button.render(self.screen, mouse)
