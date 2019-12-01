from brain_games import cli


def main(welcome, gen_question, gen_answer):
    cli.welcome()
    print(welcome, end="\n\n")
    name = cli.run()
    ROUND = 3
    for i in range(ROUND):
        question = gen_question()
        correct_answer = gen_answer(question)
        print("Question: " + question)
        print("Your answer: ", end='')
        answer = input()
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.L\
et's try again, {}!".format(answer, correct_answer, name))
            break
    else:
        print("Congratulations, {}!".format(name))
