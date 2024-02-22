names = []  # Initialize a list to store all the user inputted.
while True:
    try:
        userName = input("Name: ").capitalize()
        names.append(userName) # add the value in userName variable to names variable(list)
    except EOFError: # Exit loop if end-of-file is encountered (i.e Ctrl+D or Ctrl+Z)(EOFError is used to do the end-of-file).
        break

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}") # Display the value stored in index 0
elif len(names) == 2:
    print(f"Adieu, adieu, to {' and '.join(names)}") # Convert the names(list) into string with 'and' and display it.
else:
    print("Adieu, adieu, to ", end="")
    for i in range(len(names)):
        if i < len(names) - 2: # For names before the last two, print with a comma
            print(names[i] + ", ", end="")
        elif i == len(names) - 2: # For the second-to-last name, print with 'and' and a comma
            print(names[i] + ", and ", end="")
        else: # For the last name, print without a comma and end the line
            print(names[i])