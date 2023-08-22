userInput = input("Greeting: ").strip().lower()

"""
# Check if the userInput from the beginning of the index (first character in the 
string) to index 4 (fifth charater in the string) is equal to "hello". 
If true, go to this if statement.
"""
if userInput[0:5]=="hello":
    print("$0")
elif userInput[0]=="h" and userInput[1:5]!="ello":
    print("$20")
else:
    print("$100")