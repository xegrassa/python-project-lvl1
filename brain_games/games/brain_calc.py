import random
import operator


RULE = "What is the result of the expression?"


def creating_quiestion_and_answer():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operation, function = random.choice([
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    ])
    answer = function(number1, number2)
    return "{} {} {}".format(number1, operation, number2), str(answer)
