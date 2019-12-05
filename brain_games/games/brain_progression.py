import random


RULE = 'What number is missing in the progression?'


def creating_quiestion_and_answer():
    LENGHT_PROGRESSION = 10
    step_progression = random.randint(1, 10)
    start_progression = random.randint(1, 20)
    questions = []
    current_element = start_progression
    puzzle_number_index = random.randint(0, LENGHT_PROGRESSION-1)
    for i in range(LENGHT_PROGRESSION):
        current_element += step_progression
        if i == puzzle_number_index:
            questions.append('..')
            answer = str(current_element)
        else:
            questions.append(str(current_element))
    return ' '.join(questions), answer
