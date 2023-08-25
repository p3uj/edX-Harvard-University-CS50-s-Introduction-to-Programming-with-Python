# Problem Set 2

##### TABLE OF CONTENTS
- [1. camelCase](#1-camelcase)
  * [1. STATEMENT](#1-statement)
  * [1. MY SOLUTION](#1-my-solution)
- [2. Coke Machine](#2-coke-machine)
  * [2. STATEMENT](#2-statement)
  * [2. MY SOLUTION](#2-my-solution)
- [3. Just setting up my twttr](#3-just-setting-up-my-twttr)
  * [3. STATEMENT](#3-statement)
  * [3. MY SOLUTION](#3-my-solution)
- [4. Vanity Plates](#4-vanity-plates)
  * [4. STATEMENT](#4-statement)
  * [4. MY SOLUTION](#4-my-solution)
- [5. Nutrition Facts](#5-nutrition-facts)
  * [5. STATEMENT](#5-statement)
  * [5. MY SOLUTION](#5-my-solution)



# 1. camelCase
## 1. STATEMENT
### cameCase
#### Instruction
In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called **name**, a variable for a user’s first name might be called **firstName**, and a variable for a user’s preferred first name (e.g., nickname) might be called **preferredFirstName**.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (**_**), with all letters in lowercase. For instance, those same variables would be called **name**, **first_name**, and **preferred_first_name**, respectively, in Python.

In a file called **camel.py**, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

![Alt text](<Problem Set 2/Images/camel-case.png>)

## 1. MY SOLUTION
- [camelCase.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/3fbcd9c753005fbd37d5f9e8739dd690dba682f2/Problem%20Set%202/camel.py)


# 2. Coke Machine
## 2. STATEMENT
### Coke Machine
#### Instruction
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called **coke.py**, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

![Alt text](<Problem Set 2/Images/coke-machine.png>)

## 2. MY SOLUTION
- [Coke Machine.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/7f0296a6100e5d68330e1f7cae788d8411810c5a/Problem%20Set%202/coke.py)


# 3. Just setting up my twttr
## 3. STATEMENT
### Output removed all vowels in the string
#### Instruction
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 

In a file called **twttr.py**, implement a program that prompts the user for a **str** of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

![Alt text](<Problem Set 2/Images/twttr.png>)

## 3. MY SOLUTION
- [Output removed all vowels in the string.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/4ca974dcad1a22dc92c8af6f6a6a5814c782ba05/Problem%20Set%202/twttr.py)


# 4. Vanity Plates
## 4. STATEMENT
### Output valid if all requirements met, else invalid
#### Instruction
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

In **plates.py**, implement a program that prompts the user for a vanity plate and then output **Valid** if meets all of the requirements or **Invalid** if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein **is_valid** returns **True** if **s** meets all requirements and **False** if it does not. Assume that **s** will be a **str**. You’re welcome to implement additional functions for **is_valid** to call (e.g., one function per requirement).

![Alt text](<Problem Set 2/Images/givenCode-Vanity-Plates.png>)

**HERE'S HOW TO TEST YOUR CODE MANUALLY:**

![Alt text](<Problem Set 2/Images/testTheCode-Vanity-Plates.png>)

## 4. MY SOLUTION
- [Output valid if all requirements met, else invalid.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/f70d00829dc9567ffaa585a2f6c7d4e5cbd50b9c/Problem%20Set%202/plates.py)


# 5. Nutrition Facts
## 5. STATEMENT
### Nutrition Facts (using dict)
#### Instruction
The U.S. Food & Drug Adminstration (FDA) offers [downloadable/printable posters](https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish) that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the [FDA’s poster for fruits](https://cs50.harvard.edu/python/2022/psets/2/nutrition/Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf), which is also [available as text](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version). Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

![Alt text](<Problem Set 2/Images/nutrition-Facts.png>)

## 5. MY SOLUTION
- [Nutrition Facts (using dict).py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/537da01128a0c85fc190dd8ececf45c893cddb27/Problem%20Set%202/nutrition.py)