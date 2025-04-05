
def in_range(num, low, high):
    if num >= low and num <= high:
        return True
    
    return False


def main():
    low = int(input("Specify lower range. "))
    high = int(input("Specify higher range. "))
    number = int(input("Enter a number to check in range! "))
    print(in_range(number,low,high))


if __name__ == "__main__":
    main()