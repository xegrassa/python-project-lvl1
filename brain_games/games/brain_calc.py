from brain_games.scripts import brain_logic
import random


def main():
    welcome = "What is the result of the expression?"
    brain_logic.main(welcome, gen_question, gen_answer)


def gen_question():
    operation = random.choice(['+', '-', '*'])
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    return "{} {} {}".format(str(number_1), operation, str(number_2))


def gen_answer(question):
    number_1, operation, number_2 = question.split()
    number_1, number_2 = int(number_1), int(number_2)
    if operation == '+':
        return str(number_1 + number_2)
    elif operation == '-':
        return str(number_1 - number_2)
    else:
        return str(number_1 * number_2)


if __name__ == '__main__':
    main()
