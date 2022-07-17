import datetime
import sys
import re
import inflect

p = inflect.engine()


def main():
    dob = input("Date of Birth: ").strip()
    print(season(dob))


def season(season_string):
    date_pattern = r"(\d{4})-([0,1]\d)-([0-3]\d)"
    date_match = re.search(date_pattern, season_string)
    if date_match:
        start_date = datetime.date(int(date_match.group(1)), int(date_match.group(2)), int(date_match.group(3)))
        # get today's date
        end_date = datetime.date.today()
        # diff
        day_delta = end_date - start_date
        minute_delta = day_delta.days * 24 * 60
        minute_words = p.number_to_words(minute_delta)
        # remove the and
        and_match = r"\band\b "
        minute_words_without_and = re.sub(and_match, '', minute_words)
        return f"{minute_words_without_and.capitalize()} minutes"
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
