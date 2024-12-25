from itertools import product

schematics = [schematic.splitlines() for schematic in open("input/25.txt").read().split("\n\n")]

keys = []
locks = []
for schematic in schematics:
    current = set()
    for r, line in enumerate(schematic):
        for c, word in enumerate(line):
            if word == "#":
                current.add((r, c))
    if schematic[0][0] == "#":
        locks.append(current)
    else:
        keys.append(current)

fits = sum(1 for key, lock in product(keys, locks) if not key.intersection(lock))
print(fits)
