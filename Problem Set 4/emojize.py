import emoji
userInput = input("Input: ").strip()
if "_" in userInput:
    print(emoji.emojize("Output: " + userInput))
else:
    print(emoji.emojize("Output: " + userInput, language="alias"))