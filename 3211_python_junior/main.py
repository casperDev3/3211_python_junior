import random


def game(num):
    if num == 1:
        return "Випав орел"
    elif num == 0:
        return "Випала решка"
    else:
        return "Сталась помилка"


if __name__ == "__main__":
    # temperature = int(input("Enter temperature outside: "))
    # if temperature < -30:
    #     print("It's very cold")
    # elif 0 > temperature > -30:
    #     print("It's cold!")
    # elif temperature >= 0:
    #     print("It's warm!")
    # else:
    #     print("Some text")

    ### Conditional for game
    random_number = random.randint(0, 1)
    result = game(random_number)
    print(f"---- {result} -----")

    while True:
        print("1. Continue\n"
              "2. Break")
        ch = int(input("Enter your choice (num): "))
        if ch == 1:
            random_number = random.randint(0, 1)
            result = game(random_number)
            print(f"---- {result} -----")
            continue
        elif ch == 2:
            break
        else:
            print("Enter incorrect chosen")
            continue
