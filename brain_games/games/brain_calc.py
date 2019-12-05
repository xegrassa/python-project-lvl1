import random
import operator


RULE = "What is the result of the expression?"


def creating_quiestion_and_answer():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operation, answer = random.choice([('+', operator.add(number_1, number_2)),
                                       ('-', operator.sub(number_1, number_2)),
                                       ('*', operator.mul(number_1, number_2))
                                       ])
    return "{} {} {}".format(str(number_1), operation, str(number_2)), \
           str(answer)
