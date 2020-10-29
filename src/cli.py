from models.game_state import GameState, States
from models.pieces import PIECE_ABBREVIATIONS


def print_help():
    print(
        "The following commands are available:\n"
        "\t - start : Resets the board and starts a new game\n"
        "\t - print : Print the board and the current piece positions\n"
        "\t - help  : Show the list of all available commands\n"
        "\t - quit  : Exit the game\n"
    )

def print_new_question(square):
    print(f"\nWhich piece can go to: {square.notation}")


game_state = GameState()
new_square = None
correct_piece = None
print("\n\n::Welcome to VISU::\n\n Type `help` to see the list of available commands.\n")
while True:
    user_input = input(">>> ")

    if "help" in user_input:
        print_help()

    elif "quit" in user_input:
        break

    elif "start" in user_input:
        game_state.setup_pre_game()
        print(f"---> START <---")
        game_state.print_piece_info()

        new_square = game_state.generate_new_square()
        correct_piece = game_state.board.get_piece_that_reaches_square(new_square)
        print_new_question(new_square)
        continue

    elif "print" in user_input:
        if game_state.current_state == States.PLAY
            print(game_state.board)
        else:
            print("Nothing to display. Start a new game or type quit to exit.")
        continue


    if game_state.current_state == States.PLAY:
        if len(user_input) != 1:
            print(f"Bad input. Expected one of {PIECE_ABBREVIATIONS}")
            continue

        user_input = user_input.upper()
        if user_input not in PIECE_ABBREVIATIONS:
            print(f"Bad input. Expected one of {PIECE_ABBREVIATIONS}")
            continue

        if user_input == correct_piece.abbreviation:
            print(f"---> Correct! <---")
            game_state.update_game(correct_piece, new_square)
            new_square = game_state.generate_new_square()
            correct_piece = game_state.board.get_piece_that_reaches_square(new_square)

            print_new_question(new_square)            
        else:
            print(f"---> Game Over! <---")
            print(f"The correct piece was: {correct_piece.abbreviation}\n")
            game_state.current_state = States.GAME_OVER
