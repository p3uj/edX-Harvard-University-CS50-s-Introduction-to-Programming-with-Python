userInput = input("Input: ")
print("Output: ", end="")
for c in userInput:
    if c.upper() not in "AEIOU": # Convert string to uppercase and check whether the "AEIOU" is not present.
        print(c, end="")