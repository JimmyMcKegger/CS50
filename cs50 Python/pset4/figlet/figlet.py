# In a file called figlet.py, implement a program that:
# Expects zero or two command-line arguments:
#
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.

import sys
from pyfiglet import Figlet
import random

def random_font():
  text = input("Input: ")
  fonts = ["3-d", "5lineoblique", "acrobatic", "alligator", "basic", "bigchief", "binary", "bubble", "block", "calgphy2", "diamond", "doh", "epic", "hollywood", "jazmine",]
  font = random.choice(fonts)
  f = Figlet(font=font)
  return f.renderText(text)

def chosen_font(str):
  try:
    f = Figlet(font=str)
  except:
    wrong()
  text = input("Input: ")
  return f.renderText(text)

def wrong():
  print("Invalid usage")
  sys.exit(1)

def main():
  if len(sys.argv) < 2:
    # print('go to random')
    print(random_font())
    sys.exit(0)
  elif len(sys.argv) == 3:
    if str(sys.argv[1]) in ["-f", "--font"]:
      # print('go to choice')
      print(chosen_font(str(sys.argv[2])))
      sys.exit(0)

  wrong()

if __name__ == "__main__":
  main()