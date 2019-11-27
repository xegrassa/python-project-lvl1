from brain_games import cli


def main(welcome, gen_question, gen_answer):
    cli.welcome()
    print(welcome, end="\n\n")
    name = cli.run()
    count_correct_answer = 0
    while count_correct_answer != 3:
        question = gen_question()
        correct_answer = gen_answer(question)
        print("Question: " + question)
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
