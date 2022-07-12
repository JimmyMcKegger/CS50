# Random number guessing game
import sys
import random

def main():
  while True:
    text = input("Level: ")
    try:
      level = int(text)
    except:
      continue
    if level > 0:
      game(random.randint(0, level), level)
    else:
      continue

def game(num, max_level):
  while True:
    g = input("Guess: ")
    try:
      guess = int(g)
    except:
      continue

    if guess < 1:
      continue

    if guess == num:
      print("Just right!")
      sys.exit()
    elif guess < num:
      print("Too small!")
      continue
    else:
      print("Too large!")
      continue

if __name__ == "__main__":
  main()