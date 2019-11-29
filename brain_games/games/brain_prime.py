from brain_games.scripts import brain_logic
import random


def main():
    welcome = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_logic.main(welcome, gen_question, gen_answer)


def gen_question():
    return str(random.randint(1, 30))


def gen_answer(question):
    number = int(question)
    for i in range(2, number + 1):
        if number % i == 0 and i != number:
            return "no"
        elif i == number:
            return "yes"
    return "yes"


if __name__ == '__main__':
    main()
