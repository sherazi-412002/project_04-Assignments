import random

def main():
    print("I am Thinking about between 1 and 99")

    secret_number = random.randint(1,99)
    user_guess = int(input("Guess a Number : "))

    while user_guess != secret_number:
        if user_guess < secret_number:
            print("Your guess is to low!")
            
        else:
            print("Your guess is to high!")

        print()
        user_guess = int(input("Guess a New Number : "))

    print(f"Congrats! You guessed a right number {secret_number}")


if __name__ == "__main__":
    main()

