def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁") # Converting the :) and :( to 🙂 and 🙁
    return text # return the updated text (which is the :) and :( already replaced)

def main():
    userInput = input();result = convert(userInput) # Get user's input and call convert function
    print(result)   # Display the result

# Call to main function
main()