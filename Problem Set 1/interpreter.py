expression = input("Expression: ")
x, y, z = expression.split(" ") # In the data stored in expression, every "<space>" will separate the data for x, y, x
print(x)
print(type(x))
match y:
    case "+":
        print(f"{float(x) + float(z):.1f}")
    case "-":
        print(f"{float(x) - float(z):.1f}")
    case "*":
        print(f"{float(x) * float(z):.1f}")
    case "/":
        print(f"{float(x) / float(z):.1f}")