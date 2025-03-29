from termcolor import colored

# function performing a squre of a number which taken as an input from user
def main():
    while True:
        try:
            num: float = float(input(colored("Enter a number : ", "yellow")))
            break
        except ValueError:
            print(colored("\nPlease enter a Valid number.", "red"))
    
    print(colored(f"Square of {num} is equal to {num ** 2}", "green"))


if __name__ == "__main__":
    main()