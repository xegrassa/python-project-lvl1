import random


WELCOME = 'Answer "yes" if number even otherwise answer "no"'


def main():
    pass


def creating_quiestion_and_answer():
    number = random.randint(1, 20)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer


if __name__ == '__main__':
    main()
