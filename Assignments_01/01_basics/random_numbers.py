import random

MIN_NUMBER = 1
MAX_NUMBER = 100
NUMBER_COUNT = 10

def main():
    for _ in range(NUMBER_COUNT):
        num = random.randint(MIN_NUMBER,MAX_NUMBER)
        print(num)


if __name__ == "__main__":
    main()