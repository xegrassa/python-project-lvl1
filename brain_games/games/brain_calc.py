import random


WELCOME = "What is the result of the expression?"


def main():
    pass


def creating_quiestion_and_answer():
    operation = random.choice(['+', '-', '*'])
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    if operation == '+':
        answer = str(number_1 + number_2)
    elif operation == '-':
        answer = str(number_1 - number_2)
    else:
        answer = str(number_1 * number_2)
    return "{} {} {}".format(str(number_1), operation, str(number_2)), answer


if __name__ == '__main__':
    main()
