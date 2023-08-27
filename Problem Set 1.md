# Problem Set 1 : Conditionals

##### TABLE OF CONTENTS
- [1. Deep Thought](#1-deep-thought)
  * [1. STATEMENT](#1-statement)
  * [1. MY SOLUTION](#1-my-solution)
- [2. Home Federal Savings Bank](#2-home-federal-savings-bank)
  * [2. STATEMENT](#2-statement)
  * [2. MY SOLUTION](#2-my-solution)
- [3. File Extensions](#3-file-extensions)
  * [3. STATEMENT](#3-statement)
  * [3. MY SOLUTION](#3-my-solution)
- [4. Math Interpreter](#4-math-interpreter)
  * [4. STATEMENT](#4-statement)
  * [4. MY SOLUTION](#4-my-solution)
- [5. Meal Time](#5-meal-time)
  * [5. STATEMENT](#5-statement)
  * [5. MY SOLUTION](#5-my-solution)


# 1. Deep Thought
## 1. STATEMENT
### String user's Input and get the result of Yes or No
#### Instruction
    “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
    “You’re really not going to like it,” observed Deep Thought.
    “Tell us!”
    “All right,” said Deep Thought. “The Answer to the Great Question…”
    “Yes…!”
    “Of Life, the Universe and Everything…” said Deep Thought.
    “Yes…!”
    “Is…” said Deep Thought, and paused.
    “Yes…!”
    “Is…”
    “Yes…!!!…?”
    “Forty-two,” said Deep Thought, with infinite majesty and calm.”
    
    — The Hitchhiker’s Guide to the Galaxy, Douglas Adams

In **deep.py**, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting **Yes** if the user inputs **42** or (case-insensitively) **forty-two** or **forty two**. Otherwise output **No**.

![Alt text](<Problem Set 1/Images/deep-thought.png>)

## 1. MY SOLUTION
- [String user's Input and get the result of Yes or No.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/b44a34123cc911d156f54ef464dd121ca6e8e503/Problem%20Set%201/deep.py)


# 2. Home Federal Savings Bank
## 2. STATEMENT
### Greeting and amount output
#### Instruction
In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called **bank.py**, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output **$0**. If the greeting starts with an “h” (but not “hello”), output **$20**. Otherwise, output **$100**. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

![Alt text](<Problem Set 1/Images/bank.png>)

## 2. MY SOLUTION
- [Greeting and amount output.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/6e3afd9f2d11a072e30f28ccf01cc01159f21f8b/Problem%20Set%201/bank.py)


# 3. File Extensions
## 3. STATEMENT
### Determine the file meadia type
#### Instruction
Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called **extensions.py**, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip

If the file’s name ends with some other suffix or has no suffix at all, output **application/octet-stream** instead, which is a common default.

![Alt text](<Problem Set 1/Images/file-extensions.png>)

## 3. MY SOLUTION
- [Determine the file meadia type.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/0c9a8f9e1e0f5e5ecb0ccffdf8597f024af64890/Problem%20Set%201/extensions.py)


# 4. Math Interpreter
## 4. STATEMENT
### Math Interpreter
#### Instruction
Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called **interpreter.py**, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as **x  y  z**, with one space between **x** and **y** and one space between **y** and **z**, wherein:
- x is an integer
- y is +, -, *, or /
- z is an integer

For instance, if the user inputs **1 + 1**, your program should output **2.0**. Assume that, if **y** is **/**, then **z** will not be 0.

Note that, just as **python** itself is an interpreter for Python, so will your **interpreter.py** be an interpreter for math!

![Alt text](<Problem Set 1/Images/math-Interpreter.png>)

## 4. MY SOLUTION
- [Math Interpreter.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/2a9ddbf37bf0e07b63f79d6cf698bc79662a0923/Problem%20Set%201/interpreter.py)


# 5. Meal Time
## 5. STATEMENT
### String to float and output meal time
#### Instruction
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In **meal.py**, implement a program that prompts the user for a time and outputs whether it’s **breakfast time**, **lunch time**, or **dinner time**. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as **#:##** or **##:##**. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein **convert** is a function (that can be called by **main**) that converts **time**, a **str** in 24-hour format, to the corresponding number of hours as a **float**. For instance, given a **time** like **"7:30"** (i.e., 7 hours and 30 minutes), **convert** should return **7.5** (i.e., 7.5 hours).
![Alt text](<Problem Set 1/Images/givenCode-meal-time.png>)

![Alt text](<Problem Set 1/Images/additional-meal-time.png>)

![Alt text](<Problem Set 1/Images/meal-time.png>)

## 5. MY SOLUTION
- [String to float and output meal time.py](https://github.com/p3uj/edX-Harvard-University-CS50-s-Introduction-to-Programming-with-Python/blob/8bf96ff018418427e7ef7ec8d6131fe240b099ef/Problem%20Set%201/meal.py)