from termcolor import colored

def sum():
    print(colored("\n\t ***** Sum Of Two Numbers ***** " ,"light_magenta"))

    while True:
        try:
            num1 = int(input(colored("Enter First Number! : " , "yellow")))
            break
        except ValueError:
            print(colored("✖️  Invalid Input, Please Enter valid number.", "red"))

    while True:
        try:
            num2 = int(input(colored("Enter a second Number! : ", 'yellow')))
            break
        except ValueError:
            print(colored("✖️   Invalid Input, Please Enter valid number.", "red"))

    result = num1 + num2
    print(colored(f"\nThe Result of {num1} and {num2} = {result}", "cyan"))
    print(colored("\t----- Program Ends -----", "light_magenta"))


if __name__ == "__main__":
    sum()
   