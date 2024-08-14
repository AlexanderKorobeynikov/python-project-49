import random
import prompt
from brain_games.scripts.brain_games import main



def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = random.randint(1, 50)
        coransw = 'yes' if num % 2 == 0 else 'no'
        print(f"Question: {num}")
        ans = prompt.string('Your answer: ')
        if ans == coransw:
            i += 1
            print('Correct!')
        else:
            i = 0
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{coransw}'\n"
                  f"Let's try again, {name}!")
    print(f'Congratulations {name}!')


main()


from brain_games.cli import name


game()
