
def take_valid_word(prompt):
    while True:    
        word = input(prompt).strip()
        if word.isalpha() and len(word) >= 2:
            return word
        print("Please make sure to give letters for a complete word.")


def main():

    adjective = take_valid_word("Enter an adjective : ")
    noun = take_valid_word("Enter a Noun : ")
    verb = take_valid_word("Enter a Verb : ")        
    print(f"I saw a {adjective} {noun} trying to {verb} on the roof!")
        


if __name__ == "__main__":
    main()

