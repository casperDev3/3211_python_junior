import random

actions = ["встати", 'сісти']
questions = ["Ти вивчив все?", "Як тебе звати?", "Хто ти?"]


def game():
    # game
    while True:
        print("_____ Меню Гри ____\n\n"
              "1. Правда\n"
              "2. Дія\n\n"
              "0. Завершити гру"
              "-------------------")
        ch = int(input("Зробіть свій вибір: "))
        if ch == 1:
            print("#### Ваш вибір: Правда ###")
            variant = random.randint(0, len(questions) - 1)
            print(f"Запитання: {questions[variant]}")
            # continue
        elif ch == 2:
            print("### Ваш вибір: Дія ### ")
            variant = random.randint(0, len(actions) - 1)
            print(f"Дія: {actions[variant]}")
        elif ch == 0:
            print("_____ GAME OVER _____")
            break
        else:
            print("### Сталась помилка! ###")


if __name__ == "__main__":
    game()
