import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Wrong! Try again, not to high.")
        elif guess < random_number:
            print("Wrong! Try again, not to low.")
        elif guess == random_number:
            print(f"Jackpot!!! You guessed it, it's the number {random_number}.")

guess(10)