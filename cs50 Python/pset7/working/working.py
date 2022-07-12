import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    # pattern
    pattern = r"^(1?[0-9](?::[0-5][0-9])? [A|P]M) to (1?[0-9](?::[0-5][0-9])? [A|P]M)$"
    if time_stamps := re.search(pattern, s):
        # format start
        start = time_stamps.group(1)
        if ":" in start:
            start_hour = int(start[:-6])
            start_minutes = int(start[-5:-3])
        else:
            start_hour = int(start[:-3])
            start_minutes = None

        if start[-2] == 'P':
            start_hour = start_hour + 12
            if start_hour == 24:
                start_hour = 12
            elif start_hour > 24:
                raise ValueError

        if start_hour == 12:
            start_hour = 0

        # format end
        end = time_stamps.group(2)
        if ":" in end:
            end_hour = int(end[:-6])
            end_minutes = int(end[-5:-3])
        else:
            end_hour = int(end[:-3])
            end_minutes = None

        if end[-2] == 'P':
            end_hour = end_hour + 12
            if end_hour == 24:
                end_hour = 12
            elif end_hour > 24:
                raise ValueError
            elif end_hour == 24:
                end_hour = 0
        elif end_hour == 12:
            end_hour = 0

        if ":" not in start and ":" not in end:
            return f"{start_hour:02}:00 to {end_hour:02}:00"
        elif ":" in start and ":" in end:
            return f"{start_hour:02}:{start_minutes:02} to {end_hour:02}:{end_minutes:02}"
    raise ValueError

# print(f"{n:02}")

if __name__ == "__main__":
    main()