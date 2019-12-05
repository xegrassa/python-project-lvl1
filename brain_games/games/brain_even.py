import random


RULE = 'Answer "yes" if number even otherwise answer "no"'


def creating_quiestion_and_answer():
    number = random.randint(1, 30)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
