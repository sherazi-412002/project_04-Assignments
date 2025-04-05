
def main():
    name = input("What is Your Name? ")
    greet(name)


def greet(name: str):
    print("Hello",name,"!")


if __name__ == "__main__":
    main()