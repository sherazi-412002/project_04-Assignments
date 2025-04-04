
def main():
    fruits = {'apple':200, 'banana':100, 'jackfruit':200,'kiwi':250,'durian':300,'mango':150}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"How many {'dozen' if fruit_name == 'banana' else 'kilo'} of {fruit_name} do you want to buy? : "))
        total_cost += (price * amount_bought)

    print(f"Your total amount is {total_cost}PKR")


if __name__ == "__main__":
    main()
