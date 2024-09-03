import random
import prompt
from math import gcd
from brain_games.scripts.brain_games import main, welcome_user

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def game():
    main()
    username = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    i = 0
    while i < 3:
        num1, num2 = generate_numbers()
        correct_answer = gcd(num1, num2)
        print(f"Question: {num1} {num2}")

        answer = int(prompt.string('Your answer: '))

        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {username}!")
            i = 0

    print(f'Congratulations, {username}!')

if __name__ == '__main__':
    game()

