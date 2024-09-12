# Number Guessing game 

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100. You have 5 attempts.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Make your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you're out of attempts. The correct number was {number_to_guess}.")

number_guessing_game()
