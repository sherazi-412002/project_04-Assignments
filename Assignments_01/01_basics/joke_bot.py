
PROMPT :str = "What do You want? "
JOKE : str = "Python is like coffee. You just need one good script to stay awake."
SORRY: str = "Sorry I only tell jokes."


def main():
    user_input = input(PROMPT).strip().lower()

    if "joke" in user_input:
        print(JOKE)

    else:
        print(SORRY)


if __name__ == "__main__":
    main()