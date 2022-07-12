# asks the user for mass (in kilograms) and then outputs the equivalent number of Joules as an integer

def main():
  #convert
  m = input("m: ")
  mass = int(m)
  j = mass * (300000000 ** 2)
  print(j)

if __name__ == "__main__":
  main()