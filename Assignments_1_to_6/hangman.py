import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives to complete your word, You used these letters :", " ".join(used_letters))

        word_list = [letters if letters in used_letters else "-" for letters in word]
        print("Current Word "," ".join(word_list))

        user_letters = input("Guess a letter : ").upper()
        if user_letters in alphabets - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

            else:
                lives -= 1
                print("Letter is not in the user word")

        elif user_letters in used_letters:
            print("You already used this character. Please try again")
            
        else:
            print("Invalid Character.") 

    if lives == 0:
        print("Sorry, You died. The word was ",word ,'!!')
    else:
        print("Congrats, You Guessed the word Correctly  ", word, " In ",lives)
 



hangman()