
MAX_NUM_OF_ELE = 5

def shorten(our_list):
    while len(our_list) > MAX_NUM_OF_ELE:
        last_elem = our_list.pop()
        print("Removed Element : ",last_elem)


def get_first_element():
    
    my_list = []

    element = input("Please Write first element to list by your own or press enter to get already present element! : ")
    if element != "":
        my_list.append(element)
        element = input("Please Write first element to list by your own or press enter to get already present element! : ")
    
    return my_list


def main():
    our_list = get_first_element()
    print("Our List : ", our_list)
    shorten(our_list)
    print("Shortened List : " ,our_list)



if __name__  == "__main__":
    main()