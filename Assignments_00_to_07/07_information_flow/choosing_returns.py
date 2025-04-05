
ADULT_AGE = 18

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False

def main():
    print("(Entered Age is an adult age?)")
    age = int(input("How Old are You? : "))
    print(is_adult(age))


if __name__ == "__main__":
    main()