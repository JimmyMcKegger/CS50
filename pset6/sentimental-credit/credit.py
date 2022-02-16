import re
from sys import exit

while True:
    n = input("Number: ")
    reg = re.search("\D+", n)
    if reg:
        print("Enter a number")
    elif (len(n) < 13 or len(n) > 16):
        print("INVALID\n")
        exit(0)
    else:
        break

checkSum = False
doubles = []
singles = []

numLength = len(n)
end = len(n)-1
s = 0

while end >= 0:
    if s % 2 == 0:
        singles.append(int(n[end]))
    else:
        doubles.append(int(n[end])*2)
    s = s + 1
    end = end - 1

if (sum(singles) + sum(doubles)) % 10 == 0:
    checkSum = True

# VISA: starts with 4 and len = 13 || 16
if numLength == 13 or 16:
    if n[0] == '4':
        print("VISA\n")
        exit(0)

# AmEx: starts with 34 or 37, and len = 15
if n[0] + n[1] in ['34', '37']:
    if numLength == 15:
        print("AMEX\n")
        exit(0)

# MasterCard: starts with 51, 52, 53, 54, or 55 and len = 16
if n[0] + n[1] in ['51', '52', '53', '54', '55']:
    if numLength == 16:
        print("MASTERCARD\n")
        exit(0)

print("INVALID\n")
exit(0)