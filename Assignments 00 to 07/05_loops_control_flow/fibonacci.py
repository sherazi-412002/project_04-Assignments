
MAX_TERM_VALUE = 10000

def main():

    curret_term = 1
    next_term = 1
    while curret_term <= MAX_TERM_VALUE:
        print(curret_term)
        term_after_next = curret_term + next_term
        curret_term = next_term
        next_term = term_after_next

if __name__ == "__main__":
    main()