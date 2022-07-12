import re
import sys

def main():
    print(parse(input("HTML: ")))

"""
formats:
    http://youtube.com/embed/xvFZjo5PgG0
    https://youtube.com/embed/xvFZjo5PgG0
    https://www.youtube.com/embed/xvFZjo5PgG0
"""

def parse(s):
    # src pattern
    source = r"src=\"https?:\/\/(?:www.)?youtube.com\/embed\/(\w+)\""
    m = re.search(source, s)
    return "https://youtu.be/" + m.group(1) if m else None

if __name__ == "__main__":
    main()