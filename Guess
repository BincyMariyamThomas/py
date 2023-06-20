import random

def guess_number():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

guess_number()
