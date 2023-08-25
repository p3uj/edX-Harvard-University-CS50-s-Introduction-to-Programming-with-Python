def main():
    plate = input("Plate: ")
    if is_valid(plate): # Function call to is_valid function. And execute inside this statement if the return value is true.
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6: # Check the min and max of the characters.
        if s[:2].isalpha(): # Check if the first two characters are letters.
            if " " not in s: # Check if the string haven't spaces.
                if is_punctuation(s):   # Function call to is_punctuation function. And execute inside this statement if the return value is true.
                    if s[int(len(s) / 2 - 1)].isalpha(): # Check if the middle(int) of the string is a letter.
                        for c in s:
                            if c.isdigit(): # Check if the value of c is digit.
                                if c != "0" and s[-1].isdigit(): # Check if the value of c variable is not equal to "0" and the last character of the string is digit.
                                    return True
                                else:
                                    return False
                        return True
    return False


def is_punctuation(user_s):
    import string   # For punctuation
    for c in user_s:
        if c in string.punctuation: # Check if the value of c variable is a punctuation.
            return False
    return True

main()