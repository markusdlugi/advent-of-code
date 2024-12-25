from itertools import product

lines = [line for line in open("input/25.txt")]

keys = []
locks = []
current = set()
start_r = 0
for r, line in enumerate(lines):
    for c, word in enumerate(line):
        if line == "\n":
            start_r = r + 1
            if (0, 0) in current:
                locks.append(current.copy())
            else:
                keys.append(current.copy())
            current.clear()
        elif word == "#":
            current.add((r - start_r, c))

if (0, 0) in current:
    locks.append(current)
else:
    keys.append(current)

lock_heights = []
for l in locks:
    heights = []
    for c in range(0, 5):
        for r in range(1, 6):
            if not (r, c) in l:
                heights.append(r - 1)
                break
        else:
            heights.append(5)
    lock_heights.append(tuple(heights))

key_heights = []
for k in keys:
    heights = []
    for c in range(0, 5):
        for r in range(5, 0, -1):
            if not (r, c) in k:
                heights.append(5 - r)
                break
        else:
            heights.append(5)
    key_heights.append(tuple(heights))

fits = []
for key, lock in product(key_heights, lock_heights):
    for c in range(0, 5):
        if key[c] + lock[c] > 5:
            break
    else:
        fits.append((key, lock))

print(len(fits))
