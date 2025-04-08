from termcolor import colored

def triangle_perimeter():

    # taking inputs from user for three sides of triangle
    print(colored("\nFinding a Triangle's Perimeter\n", "light_magenta"))

    while True:
        try:
            side1: float = float(input(colored("Enter the lenght of First side in cm : ","yellow")))
            side2: float = float(input(colored("Enter the lenght of Second side in cm : ","yellow")))
            side3: float = float(input(colored("Enter the lenght of Thired side in cm : ","yellow")))
            break
        except ValueError:
            print(colored("\nPlease Enter a valid input like integers.\n", "red"))
    # calculating perimeter and printing answer 
    print(colored(f"Perimeter of Triangle is : {side1 + side2 + side3}cm\u00b3" , "green"))


if __name__ == "__main__":
    triangle_perimeter()