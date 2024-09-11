import random
import prompt
from brain_games.scripts.brain_games import main, welcome_user

# Функция для генерации арифметической прогрессии
def generate_progression():
    length = random.randint(5, 10)  # Длина прогрессии (от 5 до 10 элементов)
    start = random.randint(1, 50)  # Начальное число прогрессии
    step = random.randint(1, 10)   # Шаг прогрессии
    progression = [start + i * step for i in range(length)] 
    

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = '..'
    
    return progression, correct_answer


def game():
    main()
    username = welcome_user()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        progression, correct_answer = generate_progression()
        progression_str = ' '.join(map(str, progression))
        print(f"Question: {progression_str}")
        
        try:
            # Получаем ответ игрока
            answer = int(prompt.string('Your answer: '))
        except ValueError:
            # Если игрок ввел не число
            print(f"Invalid input. Please enter a number.")
            continue

        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {username}!")
            i = 0  # Сбрасываем прогресс при ошибке

    print(f'Congratulations, {username}!')


if __name__ == '__main__':
    game()
