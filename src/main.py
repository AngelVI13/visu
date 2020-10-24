from view import View
from models.board import Board
from controller import Controller
from game_engine import GameEngine
from event_manager import EventManager
from settings.display import DISPLAY_WIDTH, DISPLAY_HEIGHT


def main():
    game_model = Board()

    event_manager = EventManager()
    game_engine = GameEngine(event_manager)
    view = View(
        event_manager,
        game_engine,
        window_size=(DISPLAY_WIDTH, DISPLAY_HEIGHT),
        window_title="Visu",
        fps=30,
    )
    _controller = Controller(event_manager, game_engine, view, game_model)
    game_engine.run()


if __name__ == "__main__":
    main()
