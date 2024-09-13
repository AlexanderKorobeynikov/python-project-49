import random
import prompt
from brain_games.scripts.brain_games import main, welcome_user


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def game():
    main()
    username = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0
    while i < 3:
        num = random.randint(1, 100)
        print(f"Question: {num}")

        answer = prompt.string('Your answer: ').lower()


        correct_answer = "yes" if is_prime(num) else "no"

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
