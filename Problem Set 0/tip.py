def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = float(d[1:])    # Convert the data stored in dallars variable from the index 1 (second character in the string) until end (last character) into float
    return d    # return the converted data


def percent_to_float(p):
    # TODO
    p = float(p[:-1]) / 100 # Convert the data stored in percent variable from the beginning of the index (first character in the string) until index -2 (second to the last character) into float
    return p    # return the converted data


main()