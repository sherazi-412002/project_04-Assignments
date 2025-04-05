
AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():

    print(f"Please write the following Affirmation  : {AFFIRMATION}")
    user_feedback = input()

    while user_feedback != AFFIRMATION:

        print("That was not the Affirmation!")
        print(f"Please write the following Affirmation  : {AFFIRMATION}")
        user_feedback = input()


    print("That's Right :) ")


if __name__ == "__main__":
    main()

