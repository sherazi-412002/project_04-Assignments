
def average(num1,num2):
    sum = num1 + num2
    result = sum / 2

    return result

def main():
    avg_1 = average(4,7)
    avg_2 = average(8,58)

    final = average(avg_1,avg_2)

    print(f"avg_1 = {avg_1}")
    print(f"avg_2 = {avg_2}")
    print(f"final = {final}")


if __name__ == "__main__":
    main()