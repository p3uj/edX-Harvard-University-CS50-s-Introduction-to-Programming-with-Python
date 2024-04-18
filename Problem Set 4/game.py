import random

def guess_input_and_response(guess_number):
    while True:
        try:
            int_guess = int(input("Guess: "))
            if int_guess > 0:
                if int_guess < guess_number:
                    print("Too small!")
                elif int_guess > guess_number:
                    print("Too large!")
                else:
                    print("Just right!")
                    exit()
        except ValueError:
            continue

def generate_random_int(a, b):
    return random.randint(a, b)

def get_level_input():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError as e:
            continue

def main():
    # Get level input.
    level = get_level_input()
    
    # Generating random integer.
    random_integer = generate_random_int(1, level)
    
    # Prompt the user to guess the integer.
    guess_input_and_response(random_integer)

main()