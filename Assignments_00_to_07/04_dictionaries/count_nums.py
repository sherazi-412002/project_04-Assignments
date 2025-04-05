
def get_user_nums():
    list_of_nums = []
    while True:

        user_input = input("Enter a number. (Press Enter to Exit!) : ")

        if user_input == "":  
            break 
            

        try:
            user_num = int(user_input)
            list_of_nums.append(user_num)
        except ValueError:
            print("Please Enter a valid number!")
            user_input = input("Enter a number. (Press Enter to Exit!) : ")
            

    return list_of_nums

    
def num_count(nums_list):
    user_dict = {}
    for num in nums_list:
        if num not in user_dict:
            user_dict[num] = 1
        else:
            user_dict[num] += 1

    return user_dict

def print_dict(user_dict):
    for key in user_dict:
        print(f"{key} appears {user_dict[key]} times.")

def main():

    numbers_list = get_user_nums()
    if numbers_list:
        get_dict = num_count(numbers_list)
        print_dict(get_dict)
    else:
        print("No number Present")

if __name__ == "__main__":
    main()

