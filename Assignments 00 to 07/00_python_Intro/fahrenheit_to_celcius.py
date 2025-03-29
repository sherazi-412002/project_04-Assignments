from termcolor import colored

def fahrenheit_to_celcius():
    while True:
        try:
            fahrenhiet_value = float(input(colored("\n Enter a Temperature in Fahrenheit! : ",  "light_blue")))

            celcius_values = (fahrenhiet_value - 32) * 5.0/9.0

            print(colored(f"\nTemperature : {fahrenhiet_value:.2f} F is {celcius_values:.2f} C ","light_magenta"))
            break

        except ValueError:
            print(colored("Please Enter a valid number", "red"))

if __name__ == "__main__":
    fahrenheit_to_celcius()