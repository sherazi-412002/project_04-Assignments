
def addition_of_number(numbers):

    total: int = 0
    for number in numbers:
        total += number
    return total


def main():
    numbers : list[int] = [3,5,6,8,9]
    result = addition_of_number(numbers)
    print("Result of Addition: ", result)


if __name__ == "__main__":
    main()