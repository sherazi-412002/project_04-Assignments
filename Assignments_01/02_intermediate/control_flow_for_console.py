
import random 

NUMBER_OF_ROUNDS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100

def main():
    print("\t\tHigh and Low Game!")
    print("\t\t------------------")

    your_score = 0
    for i in range(NUMBER_OF_ROUNDS):    # Loop for 5 rounds 
        print("Round",i+1)
        your_number = random.randint(MIN_NUMBER,MAX_NUMBER)         # user number
        computers_number = random.randint(MIN_NUMBER,MAX_NUMBER)    # computers number
        
        print(f"Your number is {your_number}")                        # printing user number


        # Guessing user number is  higher or lower than computer and also validatate the user only type higher or lower
        while True:
            choice = input("Do you think your number is higher or lower than the computer's? ").strip().lower()
            if choice in ["higher", "lower"]:
                break
            else:
                print("❌ Invalid input! Please type 'higher' or 'lower'.")
            
        
        higher_and_correct : bool = choice == "higher"  and your_number > computers_number
        lower_and_correct : bool = choice == "lower" and your_number < computers_number

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer number was",computers_number)
            your_score += 1

        else:
            print("Aww that incorrect! The computer number was",computers_number) 
        
        print("Your Score is Now :",your_score)
        print()

    print("Thanks for Playing!")


if __name__ == "__main__":
    main()



