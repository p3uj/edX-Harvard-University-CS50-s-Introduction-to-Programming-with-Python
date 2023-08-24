print("Amount Due: 50")
changedOwed = 50

while changedOwed > 0:
    amount = int(input("Insert Coin: "))
    if amount==25 or amount==10 or amount==5:
        changedOwed -= amount
        if changedOwed > 0:
            print(f"Amount Due: {changedOwed}")
    else:
        print(f"Amount Due: 50")

if changedOwed < 0:
    changedOwed = abs(changedOwed)  # If the changedOwed value is negative, then return absolute value of changedOwed (become positive).
print("Changed Owed:", changedOwed)