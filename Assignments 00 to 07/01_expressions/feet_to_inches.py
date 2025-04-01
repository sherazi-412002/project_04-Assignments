from termcolor import colored


INCHES_IN_FOOT = 12   # Defining Conversion Factor

def main():
    while True:
        try:
            feet : float = float(input(colored("Enter a number of feet : ", "cyan")))
            inches : float = INCHES_IN_FOOT * feet  # Conversion Perfomed 
            print(colored(f"\n{feet}ft are equal to {inches}inch","yellow"))
            break
            
        except ValueError:
            print(colored("Invalid number. Please Enter a valid Number." , "red"))
    
        

if __name__ == "__main__":
    main()


