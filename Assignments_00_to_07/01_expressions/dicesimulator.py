import random

NUMBER_OF_SIDES = 6
def roll_dice(turns):

    die1 : int  = random.randint(1,NUMBER_OF_SIDES)
    die2 : int  = random.randint(1,NUMBER_OF_SIDES)
    print(f"Rolled Two dice {turns} time : die1 = {die1} and dei2 = {die2}")

def main():
    die1 = 10
    print(f"die1 in main() function in start : ",die1)
    roll_dice("1st")
    roll_dice("2nd")
    roll_dice("3rd")
    print(f"die1 value in main() is now : ",die1)  # proves that scope is unchanged


if __name__ == "__main__":
    main()

