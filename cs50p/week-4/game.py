import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
    except ValueError:
        pass
    else:
        break

random_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        pass
    else:
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large!")
        else:
            print("Just right!")
            break
