from brain_games.scripts import brain_logic
import random


def main():
    WELCOME = 'What number is missing in the progression?'
    brain_logic.main(WELCOME, gen_question, gen_answer)


def gen_question():
    LENGHT_PROGRESSION = 10
    step_progression = random.randint(1, 10)
    start_progression = random.randint(1, 20)
    end_progression = start_progression + (LENGHT_PROGRESSION * step_progression)
    progressions = []
    for i in range(start_progression, end_progression, step_progression):
        progressions.append(str(i))
    puzzle_number = random.choice(progressions)
    question = []
    for i in progressions:
        if i == puzzle_number:
            question.append('..')
        else:
            question.append(i)
    return ' '.join(question)


def gen_answer(question):
    progressions = question.split()
    index_puzzle_number = progressions.index('..')
    if index_puzzle_number > 1:
        step_progression = int(progressions[1]) - int(progressions[0])
        puzzle_number = int(progressions[0]) + \
            (step_progression * index_puzzle_number)
        return str(puzzle_number)
    else:
        step_progression = int(progressions[-1]) - int(progressions[-2])
        puzzle_number = int(progressions[-1]) - \
            (step_progression * (len(progressions) - index_puzzle_number - 1))
        return str(puzzle_number)


if __name__ == '__main__':
    main()
