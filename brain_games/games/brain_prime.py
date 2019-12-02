from brain_games.scripts import brain_logic
import random


WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    

def creating_quiestion_and_answer():
    number = random.randint(1, 30)
    for i in range(2, number + 1):
        if number % i == 0 and i != number:
            return str(number), "no"
        elif i == number:
            return str(number), "yes"


if __name__ == '__main__':
    main()
