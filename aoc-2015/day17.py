from itertools import combinations
from collections import defaultdict

containers = []
for line in open("input/17.txt"):
    container = int(line.strip())
    containers.append(container)

liters = 150
combs = defaultdict(list)
min_containers = len(containers)
for i in range(1, len(containers)):
    for comb in combinations(containers, i):
        if sum(comb) == liters:
            combs[i].append(comb)
            min_containers = min(i, min_containers)

print(sum(len(x) for x in combs.values()))
print(len(combs[min_containers]))
