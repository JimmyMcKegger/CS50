import validators
import sys


def main():
    text = input("What's your email address? ")
    print(valid(text))
    sys.exit()

def valid(s):
    return "Valid" if validators.email(s) else "Invalid"


if __name__ == "__main__":
    main()