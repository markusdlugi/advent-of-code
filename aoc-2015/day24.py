from itertools import combinations


def balance_packages(packages, group_count):
    for count in range(3, 7):
        for comb1 in combinations(packages, count):
            sum1 = sum(comb1)
            other_packages = packages.difference(comb1)
            other_sum = sum(other_packages)
            if other_sum != (group_count - 1) * sum1:
                continue
            qe = 1
            for p in comb1:
                qe *= p
            return qe


packages = set()
for line in open("input/24.txt"):
    packages.add(int(line.strip()))

print(balance_packages(packages, 3))
print(balance_packages(packages, 4))
