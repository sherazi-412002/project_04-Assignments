
def count_even(user_list):
    count = 0
    for num in user_list:
        if num % 2 == 0:
            count += 1
    print("Total count of evens in list : ",count)


def get_list_of_ints():
    user_list = []
    user_iput = input("Enter an integer or press enter to stop :) ")
    while user_iput != "":
        user_list.append(int(user_iput))
        user_iput = input("Enter an integer or press enter to stop :) ")

    return user_list

def main():
    my_list = get_list_of_ints()
    print("Here is your list! ",my_list)
    count_even(my_list)

if __name__ == "__main__":
    main()
