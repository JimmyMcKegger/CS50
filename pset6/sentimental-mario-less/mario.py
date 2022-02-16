#mario-less
from cs50 import get_int

# using a loop to validate input
while True:
    n = get_int("Height: ")
    if (n > 0 and n < 9):
        break

s = 1
while s <= n:
    # print the leading spaces
    for i in range(s, n):
        print(" ", end="")
    # print the pound signs
    print("#" * s)
    s += 1