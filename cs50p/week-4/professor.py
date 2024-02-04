import random


def main():
    level = get_level()
    score = generate_problem(level)
    print(f"Your score is {score }")


def generate_problem(level):
    score = 0
    for _ in range(1, 6):
        x, y = generate_integer(level)
        print(f"Problem: {x} + {y} ")
        answer = int(input("Answer: "))
        if answer != (x + y):
            for _ in range(1, 4):
                print("EEE")
                print(f"Problem: {x} + {y} ")
                answer = int(input("Answer: "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print(f"Correct answer: {x + y}")
        if answer == (x + y):
            score += 1
            continue
    return score


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1, 4):
                continue
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    match level:
        case 1:
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            return x, y
        case 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            return x, y
        case 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            return x, y


if __name__ == "__main__":
    main()
