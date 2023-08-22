userInput = input("File name: ").strip().lower()
if userInput[-5:] == ".jpeg":   # Check the userInput from index -5 (fifth character of the string in the right side) to end (first character of the string in the right side)
    print("image/jpeg")
    exit()
match userInput[-4:]:   # Check the userInput from index -4 (start in the right side: 4th character of the string) to end (first character of the string in the right side)
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print(f"text/{userInput[:-4]}")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")