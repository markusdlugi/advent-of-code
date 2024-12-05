from math import floor

lines = [line.strip() for line in open("input/05.txt")]

# Parse input
rules = []
updates = []
for line in lines:
    if "|" in line:
        rules.append(tuple(map(int, line.split("|"))))
    elif "," in line:
        updates.append(list(map(int, line.split(","))))

# Part 1
# Find correct & incorrect updates
correct_updates = []
incorrect_updates = []
for update in updates:
    for x, y in rules:
        try:
            xi, yi = update.index(x), update.index(y)
        except ValueError:
            continue
        if xi > yi:
            incorrect_updates.append(update)
            break
    else:
        correct_updates.append(update)

sum_of_middles = sum(update[floor(len(update) / 2)] for update in correct_updates)
print(sum_of_middles)

# Part 2
# Fix incorrect updates
for update in incorrect_updates:
    all_rules_pass = False
    while not all_rules_pass:
        all_rules_pass = True
        for x, y in rules:
            try:
                xi, yi = update.index(x), update.index(y)
            except ValueError:
                continue
            if xi > yi:
                update.remove(y)
                update.insert(xi, y)
                all_rules_pass = False

sum_of_middles = sum(update[floor(len(update) / 2)] for update in incorrect_updates)
print(sum_of_middles)
