from brain_games.scripts import brain_logic
import random
import math


def main():
    welcome = "Find the greatest common divisor of given numbers."
    brain_logic.main(welcome, gen_question, gen_answer)


def gen_question():
    return "{} {}".format(random.randint(1, 30), random.randint(10, 40))


def gen_answer(question):
    a, b = question.split()
    a, b = int(a), int(b)
    correct_answer = str(math.gcd(a, b))
    return correct_answer


if __name__ == '__main__':
    main()
