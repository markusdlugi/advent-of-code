import re

# Part A
naughty = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]
nice_words = 0
for line in open("input/05.txt"):
    is_naughty = False
    for naughty_letters in naughty:
        if naughty_letters in line:
            is_naughty = True
            break
    if is_naughty:
        continue
    vowel_count = sum([(line.count(vowel)) for vowel in vowels])
    if vowel_count < 3:
        continue
    previous_char = None
    for char in line:
        if previous_char == char:
            nice_words += 1
            break
        previous_char = char

print(nice_words)

# Part B
nice_words = 0
repeat_with_letter_in_between = r'\w*(\w)\w\1\w*'
two_letters_twice = r'\w*(\w{2})\w*\1\w*'
for line in open("input/05.txt"):
    line = line.strip()
    if not re.match(repeat_with_letter_in_between, line):
        continue
    if not re.match(two_letters_twice, line):
        continue
    nice_words += 1

print(nice_words)
