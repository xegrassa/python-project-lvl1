from brain_games import cli
import random


def main():
    print('Welcome to the Brain Games!\nAnswer \
        "yes" if number even otherwise answer "no"\n')
    name = cli.run()
    count_correct_answer = 0
    while count_correct_answer != 3:
        rnd_number = random.randint(1, 20)
        correct_answer = 'yes' if rnd_number % 2 == 0 else 'no'
        print("Question: " + str(rnd_number))
        print("Your answer: ", end='')
        answer = input()
        if answer == correct_answer:
            print('Correct!')
            count_correct_answer += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.L\
                et's try again, {}!".format(answer, correct_answer, name))
            break
    if count_correct_answer == 3:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
