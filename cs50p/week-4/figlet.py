import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Enter Text: ")
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
    print(figlet.renderText(text=text))
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Wrong command")
    else:
        text = input("Enter Text: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text=text))
else:
    sys.exit("Wrong command")
