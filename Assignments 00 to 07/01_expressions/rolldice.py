import random

NUMBER_OF_SIDES : int = 6

def main():
    print("\n\t\t Rolling a Dice Game\n")
    die1 : int = random.randint(1,NUMBER_OF_SIDES)
    die2 : int = random.randint(1,NUMBER_OF_SIDES)

    total : int = die1 + die2

    print("Dice have ",NUMBER_OF_SIDES, " sides each.")
    print("First Die : ",die1)
    print("Second Die : ",die2)
    print("Total of Two dice : ",total)


if __name__ == "__main__":
    main()
    
