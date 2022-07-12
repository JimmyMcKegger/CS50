# Converts a MM/DD/YYYY date to YYYY-MM-DD
import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
  formatted = []
  while formatted == []:
    try:
      date = input("Date: ").strip()
    except EOFError:
      exit()
    # Check what format the date is in
    pattern = "^\d{1,2}/\d{1,2}/\d{4}$"
    if re.search(pattern, date):
      #print("no_words")
      formatted = no_words(date)
    else:
      #print("has_words")
      formatted = has_words(date)

    # print and exit
  print(f"{formatted[0]:04}-{formatted[1]:02}-{formatted[2]:02}")
  exit()

def no_words(str):
  nums = str.split("/")
  m = int(nums[0])
  if m > 12:
    return []
  d = int(nums[1])
  if d > 31:
    return []
  y = int(nums[2])
  return [y, m, d]

def has_words(str):
  words = str.split()
  if words[0] not in months:
    return []
  m = int(months.index(words[0]) + 1)
  if words[1][-1] != ",":
    return []
  d = int(words[1][:-1])
  if d > 31:
    return []
  y = int(words[2])
  return [y, m, d]

if __name__  == "__main__":
  main()
