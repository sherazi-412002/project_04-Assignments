list = ["first", "second", "Third"]


def get_first_element():

    element = input("Please Write first element to list by your own or press enter to get already present element! : ")
    if element != "":
        list.insert(0,element)
    else:
        list
    return list[0]


def main():
    print("Our List : ")
    data = get_first_element()
    print("First Element of List : ", data)


if __name__  == "__main__":
    main()




