import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    if len(sys.argv) < 1 or len(sys.argv) > 3 or len(sys.argv) == 2:
        sys.exit("Invalid usage")

    # random font
    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.renderText(text))

    # requested font
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f":
            sys.exit("Invalid usage")

        font = sys.argv[2]
        try:
            figlet.setFont(font=font)
        except:
            sys.exit("Invalid usage")
            
        text = input("Input: ")
        print(figlet.renderText(text))


if __name__ == "__main__":
    main()