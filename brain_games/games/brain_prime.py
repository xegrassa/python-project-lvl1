import random
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    else:
        return True


def creating_quiestion_and_answer():
    number = random.randint(1, 30)
    if is_prime(number):
        return str(number), "yes"
    else:
        return str(number), "no"
