import random


WELCOME = 'What number is missing in the progression?'


def main():
    pass


def creating_quiestion_and_answer():
    LENGHT_PROGRESSION = 10
    step_progression = random.randint(1, 10)
    start_progression = random.randint(1, 20)
    end_progression = start_progression + \
        (LENGHT_PROGRESSION * step_progression)
    questions = []
    for i in range(start_progression, end_progression, step_progression):
        questions.append(str(i))
    puzzle_number_index = random.randint(0, LENGHT_PROGRESSION-1)
    answer = str(questions[puzzle_number_index])
    questions[puzzle_number_index] = '..'
    return ' '.join(questions), answer


if __name__ == '__main__':
    main()
