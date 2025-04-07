import random 

def play():
    user = input("\nWhat Your Choice, 'r' for rock, 's' for scissor, 'p' for paper!\n Your Choice: " )
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's Tie!"
    
    if is_win(user,computer):
        return "User Won!"
    
    return "Computer Won!"


def is_win(user,computer):
    if (user=='r' and computer == 's') or (user == 'r' and computer == 'p') or (user == 's' and computer== 'p'):
        return True
    
print(play())