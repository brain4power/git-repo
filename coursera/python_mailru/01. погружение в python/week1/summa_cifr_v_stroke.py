import sys

digit_string = sys.argv[1]

summary = 0
for letter in digit_string:
    summary += int(letter)

print(summary)
