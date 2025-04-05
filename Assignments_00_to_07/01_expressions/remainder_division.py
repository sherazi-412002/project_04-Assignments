

def main():
    while True:
        try:
            dividend : int  = int(input("Please Enter an integer to be divided : "))
            divisor : int = int(input("Enter an integer divide by : "))

            quotient : int = dividend // divisor 
            remainder : int = dividend % divisor
            print(f"The result of Division is {quotient} with a remainder of {remainder}")
            break

        except ValueError:
            print("Please Enter a Valid number.")


if __name__ == "__main__":
    main()

