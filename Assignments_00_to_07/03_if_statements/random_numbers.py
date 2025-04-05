import random

NUM_OF_TURNS = 10
MIN_NUMBER = 1
MAX_NUMBER = 100

def main():
    print("Here are 10 random numbers between 1-100")
    for _ in range(NUM_OF_TURNS):
        result = random.randint(MIN_NUMBER,MAX_NUMBER)
        print(result)

if __name__ == "__main__":
    main()
        
