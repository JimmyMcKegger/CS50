# Takes one or more names as input and bids them adieu

import inflect

p = inflect.engine()

def main():
  names = []
  while True:
    try:
      text = input("Name: ")
      names.append(text)
    except EOFError:
      print("Adieu, adieu, to ", end="")
      name_list = p.join(names)
      print(name_list)
      break

if __name__ == "__main__":
  main()