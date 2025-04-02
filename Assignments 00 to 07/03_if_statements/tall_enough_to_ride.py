
MIN_HIEGHT = 60 # Inches
def main():
    while True:
        user_hieght = input("How tall are you in inches? (Press Enter to Exit!) : ")
        if not user_hieght:
            print("Godbaye! Stay Safe!")
            break
        if user_hieght.isdigit():
            user_hieght = int(user_hieght)
            if user_hieght >= MIN_HIEGHT:
                print("You are for enogh to ride!")
            else:
                print("You are not for enough to ride. Maybe mext year.")
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()


    

