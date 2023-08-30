def main():
    items_dict = {}

    while True:
        try:
            key = input().upper()
            if key not in items_dict:
                items_dict[key] = 1 # Place the key in items_dict with the corresponding value of 1.
            else:
                items_dict[key] += 1 # Place the key in items_dict with the corresponding value of increment.
        except EOFError: # Stop the loop if the user inputted control-z or control-d
            break

    sorted_items = dict(sorted(items_dict.items())) # Sort all items in items_dict and covert it in dictionary type.

    for item in sorted_items:
        print(str(sorted_items[item]) + " " + item) # Print value and key in the sorted_items

main()