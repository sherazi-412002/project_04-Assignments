
def num_in_stock(friuts):

    if friuts == "apple":
        return 50
    elif friuts == "banana":
        return 100
    elif friuts == "durian":
        return 20
    elif friuts == "pear":
        return 1000
    else:
        return 0

def main():

    user_fruit = input("Enter a Fruit : ").lower().strip()
    stock_num = num_in_stock(user_fruit)
    if stock_num == 0:
        print(f"{user_fruit} is not in stock.")

    else:
        print(f"You fruit is present in Stock. Here's a number stock : {stock_num}")


if __name__ == "__main__":
    main()