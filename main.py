import random

secret_number = random.randint(1,100)

print("I'm thinking of a number! Try to guess the number I'm thinking of: ")
guess = int(input())
if guess < secret_number:
    print("Too low! Guess again.")
elif guess > secret_number:
    print("Too high! Guess again.")
else:
    print("That's it!")