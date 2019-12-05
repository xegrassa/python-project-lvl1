import random


RULE = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


def creating_quiestion_and_answer():
    numerator = random.randint(1, 30)
    denominator = random.randint(10, 40)
    answer = str(gcd(numerator, denominator))
    return "{} {}".format(numerator, denominator), answer
