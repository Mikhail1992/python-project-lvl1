import prompt


rounds_count = 3

def get_user_name():
    user_name = prompt.string('May I have your name? ', True)
    return 'User' if user_name is None else user_name


def runGame(title, game):
    user_name = get_user_name()
    print(f'Hello, {user_name}!')
    print(title)

    def runGameRound(round):
        (question, answer) = game()

        if round == 0:
            print(f'Congratulations {user_name}!')
            return

        print(f'Question: {question}')

        user_answer = prompt.string('Answer: ', False)

        if (user_answer != answer):
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}\nLet's try again")
            return

        print('Correct!')

        runGameRound(round - 1)

    runGameRound(rounds_count)
