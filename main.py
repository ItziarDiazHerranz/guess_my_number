import random

play_again = "yes"

while play_again.lower() == "yes":
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100!")
    guess = None
    attempts = 0
    while guess != secret_number:
        guess = int(input("Try to guess the number I'm thinking of: "))
        attempts += 1
        if guess < secret_number:
            print("Too low! Guess again.")
        elif guess > secret_number:
            print("Too high! Guess again.")
        else:
            print(f"That's it! You got it in {attempts} tries!")
    play_again = input("Would you like to play again? (yes/no)")
print("Thanks for playing!")