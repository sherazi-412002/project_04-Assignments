from termcolor import colored

# declaring friends name variables which hold friends age

ali_age: int = 23                      # ali is 23 year old
usama_age: int = ali_age + 6           # because usama is just 6 year older than ali
haider_age: int = usama_age + ali_age  # haider is old as ali's age plus usama age
horaira_age: int = ali_age             # ali and hoaraira are same aged


# function to print this all ages 

def prinAge():
    print(colored(f"\nAli is {ali_age} year old." , "yellow"))
    print(colored(f"Usama is {usama_age} year old. And is 6 year older then Ali!", "yellow"))
    print(colored(f"Haider is {haider_age} year old. And his age is equal to Ali age plus Usama age.", "yellow"))
    print(colored(f"Horaira is {horaira_age} year old.And his age equals to same as Ali", "yellow"))


if __name__ == "__main__":
    prinAge()