import re
import sys


def main():
    print(count(input("Text: ")))
    sys.exit()


def count(s):
    pattern = r"\bum\b"
    ums = re.findall(pattern, s, flags=re.IGNORECASE)
    if ums:
        return len(ums)
    else:
        return 0


if __name__ == "__main__":
    main()