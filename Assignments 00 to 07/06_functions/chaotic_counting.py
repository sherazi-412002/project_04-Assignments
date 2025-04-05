import random 

LIKELIHOOD = 0.3
def chaotic_counting():
    for curr_num in range(10):
        curr_num = curr_num + 1
        if done():
            return
        print(curr_num)

def done():
    if random.random() < LIKELIHOOD:
        return True
    return False

def main():
    print("I am going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'am Done!")


if __name__ == "__main__":
    main()