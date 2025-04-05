list = ["first", "second", "Third", "Last Element"]

def get_first_element():

    element = input("Please write last element of list by your own or press enter to get already present element! : ")
    if element != "":
        list.append(element)
    else:
        list
    return list[-1]


def main():
    print("Our List : ", list)
    data = get_first_element()
    print("Last Element of List : ", data)


if __name__  == "__main__":
    main()