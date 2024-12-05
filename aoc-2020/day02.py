from collections import Counter

lines = [line.strip() for line in open("input/02.txt")]

valid_a = valid_b = 0
for line in lines:
    policy, password = line.split(": ")
    ab, letter = policy.split(" ")
    a, b = tuple(map(int, ab.split("-")))
    count = Counter(password)[letter]
    if a <= count <= b:
        valid_a += 1
    if (password[a - 1] == letter) ^ (password[b - 1] == letter):
        valid_b += 1
print(valid_a)
print(valid_b)
