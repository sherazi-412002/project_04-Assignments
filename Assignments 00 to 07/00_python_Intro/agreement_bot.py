from termcolor import colored;


def favorite_animal():
 # This function simply take an input from user and repond with simple message
    print(colored("\t***** FAVORITE ANIMAL *****", "dark_grey"))
    animal = input(colored("Whats Your Favorite animal name? : ", "yellow"))
    
    while True:
        if animal.isalpha():
            break
        else:
            print("✖️   Only letters are allowed.")

        if len(animal) < 3:
            print(f"At least 3 characters required.")
            break

        if len(animal) > 20:
            print(f"The upper limit of characters is 19.")
            break

    print(colored(f"My Favorite animal is {animal}!", "cyan"))


if __name__ == "__main__":
    favorite_animal()


        