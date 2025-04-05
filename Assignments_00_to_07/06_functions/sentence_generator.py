
def make_sentence(word, part_of_speech):
    if part_of_speech == 1:
        print(f"I just found the perfect {word} to complete my collection!")
    elif part_of_speech == 2:
        print(f"The weather's amazing — I just want to go out and {word}!")
    elif part_of_speech == 3:
        print(f"Wow, the sky looks incredibly {word} this evening.")
    else:
        print("Invalid part of speech! Please enter 0 for noun, 1 for verb, or 2 for adjective.")


def main():
    word = input("Please type a noun, verb, or adjective: ")
    try:
        part_of_speech = int(input("Is this a noun, verb, or adjective? Type 1 for noun, 2 for verb, 3 for adjective: "))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("Invalid input! Please enter a number for part of speech.")

if __name__ == "__main__":
    main()