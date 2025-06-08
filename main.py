import random

secret_number = random.randint(1,100)

print("I'm thinking of a number between 1 and 100!")
guess = None
while guess != secret_number:
    guess = int(input("Try to guess the number I'm thinking of: "))
    if guess < secret_number:
        print("Too low! Guess again.")
    elif guess > secret_number:
        print("Too high! Guess again.")
    else:
        print("That's it!")