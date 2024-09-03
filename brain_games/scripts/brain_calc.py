import random
import prompt
from brain_games.scripts.brain_games import main, welcome_user

def generate_operator():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return f"{num1} {operator} {num2}", correct_answer

def game():
    main()
    username = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        expression, correct_answer = generate_operator ()
        print(f"Question: {expression}")
        answer = int(prompt.string('Your answer: '))

        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {username}!")
            i = 0

    print(f'Congratulations, {username}!')

if __name__ == '__main__':
    game()
