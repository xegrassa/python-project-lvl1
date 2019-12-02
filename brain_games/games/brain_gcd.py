from brain_games.scripts import brain_logic
import random
import math


WELCOME = "Find the greatest common divisor of given numbers."


def main():
    pass


def creating_quiestion_and_answer():
    numerator = random.randint(1, 30)
    denominator = random.randint(10, 40)
    answer = str(math.gcd(numerator, denominator))
    return "{} {}".format(numerator, denominator), answer


if __name__ == '__main__':
    main()
