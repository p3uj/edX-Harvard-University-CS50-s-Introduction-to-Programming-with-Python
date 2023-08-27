def main():
    result = compute()  # Function call to compute() function.
    if result <= 1:
        print("E")
    elif result == 99 or result == 100:
        print("F")
    elif result > 101:
        compute()
    else:
        print(f"{result}%")


def compute():
    while True:
        try:
            x, y = (input("Fraction: ")).split("/") # Get the user input and separate that for x and y. "/" is a separation cue.
            result = int(x) / int(y) * 100
            result = round(result)
        except (ValueError, ZeroDivisionError): # Execute this statement if the user input is not an integer.
            pass    # Does nothing.
        else:
            return result
main()