"""
Module that defines & implements game engine logic (game initialization,
state machine handling & tick event generation)
"""
import pygame

from event import *
from state import StateMachine, States
from event_manager import Listener, EventManager
from models.board import Board
from models.game_state import GameState


class GameEngine(Listener):
    """GameEngine class that manages game initialization,
    states machine & tick event generations.
    """

    def __init__(self, event_manager: EventManager):
        super().__init__(event_manager)

        self.running = False
        self.state = StateMachine()
        self.game_state = GameState()

    def _pop_state(self):
        """Remove state from state machine. If no states
        are left in the state machine - quit the game.
        """
        # pop current state
        self.state.pop()

        # if not states are left -> quit the game
        if self.state.peek() is None:
            self.event_manager.post(QuitEvent())

    def notify(self, event: Event):
        """Triggered when an event is submitted to the message
        queue.
        """
        if isinstance(event, QuitEvent):
            self.running = False

        elif isinstance(event, StateChangeEvent):
            if event.state == States.POP:
                self._pop_state()
                return  # do not store POP state on the stack

            elif event.state == States.PLAY:
                # when state changes to "PLAY" setup the in-game state machine
                self.game_state.setup_pre_game()

            self.state.push(event.state)

    def run(self):
        """Start & run the game engine loop.
        Pumps a TickEvent into the message queue for each loop.
        The loop ends when the game engine sees a QuitEvent in notify()
        """
        self.running = True
        self.event_manager.post(InitializeEvent())

        # push initial state to the state stack
        self.state.push(States.MENU)

        while self.running:
            tick = TickEvent()
            self.event_manager.post(tick)


if __name__ == "__main__":
    from unittest.mock import MagicMock

    mock_event_manager = MagicMock()

    game_engine = GameEngine(mock_event_manager)
    assert game_engine.running is False
    assert isinstance(game_engine.state, StateMachine)
