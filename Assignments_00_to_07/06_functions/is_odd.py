
def is_odd(value : int ):
    remaider = value % 2
    return remaider == 1

def main():
    print("\nIdentifying the 10 integers either even or odd!\n")
    for i in range(10):
        if is_odd(i):
            print(f"{i} is odd!")
        else:
            print(f"{i} is Even!")

if __name__ == "__main__":
    main()