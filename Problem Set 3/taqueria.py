menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
item = 0
total = 0
while True:
    try:
        userOrder = input("Item: ").title()
        if userOrder in menu:
            item += 1
            total += menu[userOrder]
        if item == 1 and total >= 9.50:
            print(f"Total: ${total:.2f}")
        elif item == 3:
            print(f"Total: ${total:.2f}")
    except EOFError: # Exit loop if end-of-file is encountered (i.e Ctrl+D or Ctrl+Z)(EOFError is used to do the end-of-file).
        break
print(f"Total: ${total:.2f}")