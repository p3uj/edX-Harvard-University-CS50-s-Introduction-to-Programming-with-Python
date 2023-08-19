answer = input("What is the Answer to the Great Question of Life, the Universe and Everthing? ").strip()
if answer=="Forty Two" or answer=="forty-two" or answer=="42" or answer=="forty two":
    print("Yes")
elif answer[0:3]=="FoR" or answer[0:3]=="fOr" or answer[0:3]=="FOR":
    print("Yes")
else:
    print("No")