
# define a function for accessing index from list
def access_index(list, index):
    try:
        return list[index]
    except IndexError:
        print("Index is out of range.")

# difine a function for modifying a list
def modify_element(list,index,new_value):
    try:
        list[index] = new_value
        return list 
    except IndexError:
        print("Index is out of range.")

# define a fuction to slice the list
def slice_list(list,start,end):
    try:
        sliced_list = list[start:end]
        return sliced_list
    except IndexError:
        print("Index is out of range.")


def main():
    my_list = [1,2,3,4,5]
    print("Here is Our List :",my_list)
    print("Choose an operation : access , modify , slice ")
    operation = input("Enter an operation: ").strip().lower()

    if operation == "access":
        index = int(input("Enter an index to access: "))
        accessed_element = access_index(my_list,index)
        print("Accessed Element :",accessed_element)

    elif operation == "modify":
        index = int(input("Enter an index: "))
        new_value = input("Enter a new value: ")
        print("Modified List :",modify_element(my_list,index,new_value))

    elif operation == "slice":
        start = int(input("Enter a start index: "))
        end = int(input("Enter an end index: "))
        print("Sliced list :",slice_list(my_list,start,end))

    else:
        print("Invalid Operation.")


if __name__ == "__main__":
    main()

