from brain_games.scripts.brain_logic import start_game
from brain_games.games import brain_calc


def main():
    start_game(brain_calc.WELCOME, brain_calc.creating_quiestion_and_answer)


if __name__ == '__main__':
    main()
