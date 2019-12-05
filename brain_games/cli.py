import prompt


def take_name():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def welcome():
    print("Welcome to the Brain Games!")
