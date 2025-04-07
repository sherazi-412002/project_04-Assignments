import random
import string

def generate_password(length=8, isDigits=True,isSpecialCharacter=True):
    
    special_chars = "@#$%&"

    #First we select at least 1 character from each 
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits) if isDigits else random.choice(string.ascii_letters),
        random.choice(special_chars) if isSpecialCharacter else random.choice(string.ascii_letters)
    ]

    characters = string.ascii_letters

    if isDigits:
        characters += string.digits
    if isSpecialCharacter:
        characters += special_chars
        
    password = ''.join(random.choice(characters) for _ in range(length))
    # random.shuffle(password)
    return password

length = int(input("Enter a password length! "))
if length < 4:
    print("Password length must be at least 4 to include all character types.")
else:
    isDigits = input("Include Digits? ('y' for Yes, 'n' for No.)  ").lower() == 'y'
    isSpecialCharacter = input("Include SpecialCharacter? ('y' for Yes, 'n' for No.)  ").lower() == 'y'
    print("Generated Password  ",generate_password(length,isDigits,isSpecialCharacter))