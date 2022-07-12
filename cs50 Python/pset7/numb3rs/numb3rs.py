# validates IPv4 addresses

import re
import sys


def main():
    print(str(validate(input("IPv4 Address: "))))


def validate(ip):
    pattern = r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    return True if re.search(pattern, ip.strip()) else False


if __name__ == "__main__":
    main()