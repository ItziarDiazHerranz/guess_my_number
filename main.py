import random

def play_game():
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100!")

    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Try to guess the number I'm thinking of: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Guess again.")
            elif guess > secret_number:
                print("Too high! Guess again.")
            else:
                print(f"That's it! You got it in {attempts} tries!")
        except ValueError:
            print("That's not a number! Try again.")

def main():
    play_again = "yes"

    while play_again.lower() == "yes":
        play_game()
        play_again = input("Would you like to play again? (yes/no): ")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
