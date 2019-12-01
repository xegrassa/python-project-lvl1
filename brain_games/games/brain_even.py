from brain_games.scripts import brain_logic
import random


def main():
    WELCOME = 'Answer "yes" if number even otherwise answer "no"'
    brain_logic.main(WELCOME, gen_question, gen_answer)


def gen_question():
    return str(random.randint(1, 20))


def gen_answer(question):
    correct_answer = 'yes' if int(question) % 2 == 0 else 'no'
    return correct_answer


if __name__ == '__main__':
    main()
