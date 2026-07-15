import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))

    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Congratulations!")
        break