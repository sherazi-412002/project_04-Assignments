
def main():

    numbers : list[int] = [1,2,3,4,5]

    print("Original List : ", numbers)
    for i in range(len(numbers)):
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 2

    print("\nDoubled List : ", numbers)


if __name__ == "__main__":
    main()