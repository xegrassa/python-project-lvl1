from brain_games import cli


NUMBER_OF_ROUND = 3


def start_game(game):
    cli.welcome()
    print(game.RULE)
    print()
    name = cli.take_name()
    for _ in range(NUMBER_OF_ROUND):
        question, correct_answer = game.creating_quiestion_and_answer()
        print("Question: " + question)
        answer = input("Your answer: ")
        if answer != correct_answer:
            print(
            	"'{}' is wrong answer ;(. Correct answer was '{}'."
            	"Let's try again, {}!".format(answer, correct_answer, name)
            	)
            break
        print('Correct!')
    else:
        print("Congratulations, {}!".format(name))
