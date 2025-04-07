import random

def computer_guess(num):
    low = 1
    high = num
    feedback = ''
    print(f"\nThink a number between 1 to {high}, Computer will Guess Your Number\n")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} is Too low (L) , Too high (H), or Correct (C) ??  ").lower() 
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1 
    
    print(f"Congrats, The Computer Guessed a number {guess}, Correctly!")


computer_guess(10)