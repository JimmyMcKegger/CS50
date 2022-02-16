from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change > -1:
        break

cents = int(change*100)
quarters = dimes = nickels = pennies = 0

# calculate quarters
if cents >= 25:
    quarters = cents // 25
    #print(f"q: {quarters}")
    cents = cents % 25

# calculate dimes
if cents >= 10:
    dimes = cents // 10
    #print(f"d: {dimes}")
    cents = cents % 10

# calculate nickels
if cents >= 5:
    nickels = cents // 5
    #print(f"n: {nickels}")
    cents = cents % 5

# calculate pennies
pennies = cents
#print(f"p: {pennies}")

coins = [quarters, dimes, nickels, pennies]
print(sum(coins))