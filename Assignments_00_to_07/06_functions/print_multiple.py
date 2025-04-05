import string
def print_muntiple():
    user_input = input("Enter a message : ")
    no_of_repeats = int(input("Enter a number of repeats : "))
    multipled_message = user_input * no_of_repeats
    print(multipled_message)

def main():
    print_muntiple()

if __name__ == "__main__":
    main()