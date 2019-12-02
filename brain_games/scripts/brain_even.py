from brain_games.scripts.brain_logic import start_game
from brain_games.games import brain_even 


def main():
    start_game(brain_even.WELCOME, brain_even.creating_quiestion_and_answer)


if __name__ == '__main__':
    main()
