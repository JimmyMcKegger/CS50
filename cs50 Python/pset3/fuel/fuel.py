# Takes a fraction and returns a percentage
import sys

def convert(fraction):
  while True:
    try:
      x, y = fraction.split('/')
      numerator = int(x)
      denominator = int(y)
      res = numerator / denominator
      if res <= 1:
        return int(res * 100)
      else:
        fraction = input("Fraction: ")
        pass
    except (ValueError, ZeroDivisionError):
      # fraction = input("Fraction: ")
      raise

def gauge(p):
  if p < 2:
    return "E"
  elif p > 98:
    return "F"
  else:
    return str(p) + "%"

def main():
    fuel = input("Fraction: ")
    frac = convert(fuel)
    print(gauge(frac))

if __name__ == "__main__":
  main()