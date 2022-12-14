import prompt


def call_dialog(logic):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(logic.QUESTION)
    counter = 0
    while counter < 3:
        example, right_answer = logic.get_game()
        print(f'Question: {example}')
        answer = prompt.string('Your answer: ')

        if right_answer == answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if counter == 3:
        print(f'Congratulations, {name}!')
