from brain_games.scripts.brain_logic import start_game
from brain_games.games import brain_progression


def main():
    start_game(brain_progression.WELCOME,
               brain_progression.creating_quiestion_and_answer)


if __name__ == '__main__':
    main()
