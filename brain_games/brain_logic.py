from brain_games import cli


def start_game(game):
    cli.welcome()
    print(game.RULE, end="\n\n")
    name = cli.take_name()
    ROUND = 3
    for i in range(ROUND):
        question, correct_answer = game.creating_quiestion_and_answer()
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
