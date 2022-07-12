# Sells coke by the can

def main():
  denominations = (5, 10, 25)
  count = 50
  change = "0"
  coin = 0
  while count > 0:
    print("Amount Due: " + str(count))
    coin = int(input("Insert coin: "))

    if coin in denominations:
      count -= coin

    if count < 0:
      change = str(abs(count))

  print("Change Owed: " + change)

if __name__ == "__main__":
  main()