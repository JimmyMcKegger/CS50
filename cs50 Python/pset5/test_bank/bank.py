# Checks greeting and outputs the amount of money owed

def value(greeting):
    if greeting[:5] == "Hello":
      return 0
    elif greeting[0] == "H":
      return 20
    else:
      return 100

def main():
  greeting = input("Greeting: ").strip()
  result = value(greeting)
  print(f'${str(result)}')

if __name__ == "__main__":
  main()