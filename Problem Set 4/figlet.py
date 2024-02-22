from pyfiglet import Figlet
import sys
import random

def main():
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] in ['-f', '--font']:
                if len(sys.argv) > 2:
                    f = Figlet(font=sys.argv[2])
                else:
                    f = Figlet(font=random.choice(Figlet().getFonts()))
            else:
                raise ValueError("Invalid usage")
        else:
            f = Figlet(font=random.choice(Figlet().getFonts()))
    except ValueError as e:
        print(e)
        sys.exit(1)

    string_val = input('Input: ')
    print('Output:')
    print(f.renderText(string_val))

if __name__ == "__main__":
    main()