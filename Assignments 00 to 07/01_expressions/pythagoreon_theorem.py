import math


def main():
    while True:
        try:
            ab : float = float(input("Enter the length of AB (The Base) : "))
            ac : float = float(input("Enter the length of Ac (The Perpendicular) : "))
            bc : float = math.sqrt((ab ** 2) + (ac ** 2) )
        except ValueError:
            print("Invalid Number.. Please Enter a valid number.")

        print(f"Length of side BC (The Hypotenouse) is : {bc:.1f}")
        break

if __name__ == "__main__":
    main()