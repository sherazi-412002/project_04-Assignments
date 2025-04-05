def double_a_number(num : int):
    return num * 2


def main():
    input_num = int(input("Enter an integer : "))
    doubled_num = double_a_number(input_num)
        
    print(f"Doubled Number = {doubled_num}")


if __name__ == "__main__":
    main()
