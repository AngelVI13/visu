import pygame

from event import *
from view import View
from models.board import Board
from game_engine import GameEngine
from controllers.pointer import Pointer
from controllers.keyboard import Keyboard
from event_manager import Listener, EventManager


class Controller(Listener):
    def __init__(self, event_manager: EventManager, game_engine: GameEngine, view: View, game_model: Board):
        super().__init__(event_manager)
        self.game_engine = game_engine
        self.game_model = game_model

        self.keyboard = Keyboard(event_manager, game_engine, view)
        self.pointer = Pointer(event_manager, game_engine, view, game_model)

    def notify(self, event: Event):
        # Controller event handling is only performed on TickEvents
        if not isinstance(event, TickEvent):
            return

        for event in pygame.event.get():
            # handle window manager closing the window (X-button click)
            if event.type == pygame.QUIT:
                self.event_manager.post(QuitEvent())

            # handle key presses
            elif event.type == pygame.KEYDOWN:
                self.keyboard.handle_keydown(event)

            # handle mouse clicks
            elif event.type == pygame.MOUSEBUTTONUP:
                self.pointer.handle_mouseup(event)

            # handle mouse motion - used for button highlighting
            elif event.type == pygame.MOUSEMOTION:
                self.event_manager.post(MouseEventMove(event.pos))
