# Validates text for vanity plates
import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
  # check for whitespace, and length
  if re.search(r"^[\S\w\d]{2,6}$", s):
    # no special characters
    if not re.search(r"[\.\!\,\?\\\/]", s):
      # All vanity plates must start with at least two letters.
      if s[:2].isalpha():
        # Check if there are numbers
        nums =  re.search(r"\d", s)
        if nums == None:
          return True
        # The first number used cannot be a ‘0’.
        elif  not s[nums.start()] == '0':
          # no letters between the first and end of string
          if not re.search(r"\D", s[nums.start():-1]):
            return True
  return False

if __name__ == "__main__":
  main()