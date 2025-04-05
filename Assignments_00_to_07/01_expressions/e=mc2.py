from termcolor import colored
C = 299792458 

# function calculate the energy in joules by taking mass in kg from user
def main():
    print(colored("\n\t\t\tMass to Joules Convertor (e=mc^2)\n" , "light_magenta"))
    while True:
        try:
            mass_in_kg = float(input(colored("Enter values in Kilos : ", "yellow")))
            break
        except ValueError:
            print(colored("\nInvalid number. Please enter a valid number","red"))
     # Calculation        
    energy_in_joules = mass_in_kg * (C ** 2)
    print(colored(f"\n{mass_in_kg} kg is equal {energy_in_joules:.3e} joules of energy!" ,"green"))


if __name__ == "__main__":
    main()



    
