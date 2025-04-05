
def print_one_digit(num):
    print(f"The One Digit is {num % 10}")

def main():
    num = int(input("Enter a number : "))
    print_one_digit(num)


if __name__ == "__main__":
    main()