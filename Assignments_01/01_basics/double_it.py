
def double_the_number(user_value):
    while user_value < 100:
        user_value = user_value * 2
        print(user_value)

def main():
    print("The Program doubles the user's number until the number reaches 100\n")
    user_value = int(input("Enter a number : "))

    if user_value < 100:
        double_the_number(user_value)
      
    else:
        print("Enter a number between 1-100")
        user_value = int(input("Enter a number : "))

if __name__ == "__main__":
    main()