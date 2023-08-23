def main():
    time = convert(input("What time is it? "))
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")    # Separate the value for time and minutes
    if minutes[-4:].lower() == "a.m." or minutes[-4:].lower() == "p.m.":    # Execute this if statement if the last four characters of minutes are "a.m." or "p.m.".
        minutes, status = minutes.split(" ")    # Separate the value for minutes (numbers) and value for status (am or pm) withe the <space> as the separation cue.
    if minutes == "00":
         result = float(hours) + float(minutes)
    else:
        result = 1.0 / (60/float(minutes)) + float(hours)   # Convert the value of hours and minutes to float then compute
    return result

if __name__ == "__main__":
    main()