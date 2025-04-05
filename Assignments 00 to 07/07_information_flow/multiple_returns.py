
def get_user_info():
    first_name = input("Enter Your First Name. : ")
    last_name = input("Enter Your Last Name. : ")
    email = input("Enter Your Email Adress. : ")

    return first_name, last_name, email

def main():
    first,last,email = get_user_info()
    print(f"We Recived User's Data : First Name: {first}, Last Name: {last}, and Email Adress: {email}")


if __name__ == "__main__":
    main()

