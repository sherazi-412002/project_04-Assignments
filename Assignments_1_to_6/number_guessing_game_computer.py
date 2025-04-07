import random 


def guess(num):
    random_number = random.randint(1,num)
    guess_number = 0

    while (random_number != guess_number):
        guess_number = int(input(f"Guess a number between 1 and {num} :  "))
        if random_number < guess_number:
            print("Sorry, Guess Again, Your Guess is too High!")
        elif random_number > guess_number:
            print("Sorry, Guess Again, Your Guess is too Low!")
    print(f"Congrats, You guessed a number {random_number} correctly.")


guess(10)