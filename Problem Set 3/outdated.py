m = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        userInput = input("Date: ").strip().title()
        if "/" in userInput:
            month, day, year = userInput.split("/") # Separate the value for month, day, year.
            if (len(year)==4) and (len(month)<=2 and int(month)<=12) and (len(day)<=2 and int(day)<=31): # If the user inputted correct format (i.e month-day-year—like 7/7/2002 or July 7, 2002).
                month, day, year = int(month), int(day), int(year) # Covert month, day, year to int.
                break
        elif "," in userInput:
            month, day, year = userInput.split(" ") # Separate the value for month, day, year.
            day, u = day.split(",") # Update the value of day. Removed the comma in the value of day.
            if month.isalpha():
                month = str(m.index(month) + 1) # Get the month index in the list of m then add 1. Covert the result to string.            
            if (len(year)==4) and (len(month)<=2 and int(month)<=12) and (len(day)<=2 and int(day)<=31): # If the user inputted correct format (i.e month-day-year—like 7/7/2002 or July 7, 2002).
                month, day, year = int(month), int(day), int(year)  # Covert month, day, year to int.
                break
        else:
            continue # Does nothing. Continue the loop.
    except ValueError:
        break

print(f"{year}-{month:02}-{day:02}") # Print the result in the format of year, month, day. And if the month and day digit are 1, add 0 before the number. Max of 2 digits for month and day.