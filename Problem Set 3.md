# Problem Set 3 : Exceptions

##### TABLE OF CONTENTS
- [1. Fuel Gauge](#1-fuel-gauge)
  * [1. STATEMENT](#1-statement)
  * [1. MY SOLUTION](#1-my-solution)
- [2. Felipe's Taqueria](#2-felipe-s-taqueria)
  * [2. STATEMENT](#2-statement)
  * [2. MY SOLUTION](#2-my-solution)
- [3. Grocery List](#3-grocery-list)
  * [3. STATEMENT](#3-statement)
  * [3. MY SOLUTION](#3-my-solution)
- [4. Outdated](#4-outdated)
  * [4. STATEMENT](#4-statement)
  * [4. MY SOLUTION](#4-my-solution)



# 1. Fuel Gauge
## 1. STATEMENT
### Fuel Gauge
#### Instruction
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called **fuel.py**, implement a program that prompts the user for a fraction, formatted as **X/Y**, wherein each of **X** and **Y** is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output **E** instead to indicate that the tank is essentially empty. And if 99% or more remains, output **F** instead to indicate that the tank is essentially full.

If, though, **X** or **Y** is not an integer, **X** is greater than **Y**, or **Y** is **0**, instead prompt the user again. (It is not necessary for **Y** to be **4**.) Be sure to catch any exceptions like **ValueError** or **ZeroDivisionError**.

![Alt text](<Problem Set 3/Images/fuel-Gauge.png>)

## 1. MY SOLUTION
- [Fuel Gauge.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/3fb935d8654ce6c517e890de36ae708473c52079/Problem%20Set%203/fuel.py)


# 2. Felipe's Taqueria
## 2. STATEMENT
### Users input orders by listing items one per line until they use control-z to stop
#### Instruction
One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the **dict** below, wherein the value of each key is a price in dollars:

    {
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

In a file called **taqueria.py**, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d or control-z(which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign (**$**) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

**HERE'S HOW TO TEST YOUR CODE MANUALLY**
![Alt text](<Problem Set 3/Images/felipes-taqueria.png>)

## 2. MY SOLUTION
- [Users input orders by listing items one per line until they use control-z to stop.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/c29eec4bfb08861717c1992f3d86a79544c2c4fb/Problem%20Set%203/taqueria.py)


# 3. Grocery List
## 3. STATEMENT
### Grocery List (using dict)
#### Instruction
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called **grocery.py**, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

![Alt text](<Problem Set 3/Images/grocery-list.png>)

## 3. MY SOLUTION
- [Grocery List (using dict).py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/8b6eaff60d18174a2fc2cdbbebfbf92623f3eec7/Problem%20Set%203/grocery.py)


# 4. Outdated
## 4. STATEMENT
### Outdated
#### Instruction
In the United States, dates are typically formatted in [month-day-year order](https://en.wikipedia.org/wiki/Date_and_time_notation_in_the_United_States) (MM/DD/YYYY), otherwise known as [middle-endian](https://en.wikipedia.org/wiki/Endianness#Middle-endian) order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called **outdated.py**, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like **9/8/1636** or **September 8, 1636**, wherein the month in the latter might be any of the values in the **list** below:

    [
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

Then output that same date in **YYYY-MM-DD** format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

**HERE'S HOW TO TEST YOUR CODE MANUALLY**
![Alt text](<Problem Set 3/Images/outdated.png>)

## 4. MY SOLUTION
- [Outdated.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/e139617b43486d8af54d39edccf9ca3025c612c9/Problem%20Set%203/outdated.py)