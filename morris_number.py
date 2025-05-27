"Morris Number Sequence"

def morris_number(term):
    current = "1"

    for _ in range(1, term):
        next_term = ""
        index = 0

        while index < len(current):
            repeat = 1

            while index + repeat < len(current) and current[index + repeat] == current[index]:
                repeat += 1

            next_term += str(repeat) + current[index]
            index += repeat

        current = next_term

    return print(current)

if __name__ == "__main__":
    term = int(input("What term of the Morris Number Sequence do you want to print? "))
    morris_number(term)
