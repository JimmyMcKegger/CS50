from cs50 import get_string
import re

text = get_string("Text: ")

letters = 0
words = 1 # add an extra one because we're starting on teh first word
sentences = 0

for l in text:
    if re.search("\w", l):
        letters += 1

    if re.search("\s", l):
        words += 1

    if re.search("[.!?]", l):
        sentences += 1

# L is the average number of letters per 100 words
L = 100 * float(letters) / float(words)

# S is the average number of sentences per 100 words in the text.
S = 100 * float(sentences) / float(words)

readingLevel = round(0.0588 * L - 0.296 * S - 15.8)

if readingLevel < 1:
    print("Before Grade 1")
elif 1 <= readingLevel < 16:
    print(f"Grade {readingLevel}")
else:
    print("Grade 16+")