import random

def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 0
        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == (x + y):
                    score += 1
                    break
                else:
                    if tries == 2:
                        print(f"{x} + {y} = {x + y}")
                        break
                    else:
                        print("EEE")
                        tries += 1
                        continue
            except ValueError:
                print("EEE")
                if tries == 3:
                    break
                else:
                    tries += 1
                    continue
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1,2,3]:
                break
        except:
            pass
    return lvl

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()