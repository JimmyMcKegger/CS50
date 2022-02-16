# mario-more
# using a loop to validate input
while True:
    try:
        n = int(input("Height: "))
        if (n > 0 and n < 9):
            break
    except ValueError:
        print("Input a number between 1 and 8.")


s = 1
while s <= n:
    # print the leading spaces
    for i in range(s, n):
        print(" ", end="")
    # print the initial pound signs
    print("#" * s, end="")
    # middle spaces
    print("  ", end="")
    # print the ending pound signs
    print("#" * s, end="")
    s += 1
    print()