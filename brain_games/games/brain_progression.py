from brain_games.scripts import brain_logic
import random


def main():
    welcome = 'What number is missing in the progression?'
    brain_logic.main(welcome, gen_question, gen_answer)


def gen_question():
    count_number = 10
    step_progression = random.randint(1, 10)
    start_progression = random.randint(1, 20)
    end_progression = start_progression + (count_number * step_progression)
    progression = []
    for i in range(start_progression, end_progression, step_progression):
        progression.append(str(i))
    puzzle_number = random.choice(progression)
    question = []
    for i in progression:
        if i == puzzle_number:
            question.append('..')
        else:
            question.append(i)
    return ' '.join(question)


def gen_answer(question):
    progression = question.split()
    index_puzzle_number = progression.index('..')
    if index_puzzle_number > 1:
        step_progression = int(progression[1]) - int(progression[0])
        puzzle_number = int(progression[0]) + \
            (step_progression * index_puzzle_number)
        return str(puzzle_number)
    else:
        step_progression = int(progression[-1]) - int(progression[-2])
        puzzle_number = int(progression[-1]) - \
            (step_progression * (len(progression) - index_puzzle_number - 1))
        return str(puzzle_number)


if __name__ == '__main__':
    main()
