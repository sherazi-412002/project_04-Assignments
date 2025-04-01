
def main():

    my_list = []
    list_item = input("Enter item to add in list or press enter to print list : " )
    while list_item:
        my_list.append(list_item)
        list_item = input("Enter item to add in list or press enter to print list : " )

    print(my_list)


if __name__ == "__main__":
    main()

