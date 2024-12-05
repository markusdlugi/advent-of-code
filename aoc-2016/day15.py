import re
from timeit import default_timer as timer


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    d, s, t = extended_euclid(b, a % b)
    return d, t, s - (a // b) * t


def chinese_remainder(modulos):
    M = 1
    for m, a in modulos:
        M *= m

    x = 0
    for m, a in modulos:
        Mi = M // m
        x += extended_euclid(m, Mi)[2] * Mi * a

    return x + (-1 * (x // M) * M) if x < 0 else x


pattern = r'(\d+) positions; at time=0, it is at position (\d+)'
modulos = []
for i, line in enumerate(open("input/15.txt")):
    mod, pos = tuple(map(lambda x: [int(n) for n in x], re.findall(pattern, line)))[0]
    target = (2 * mod - (pos + i + 1)) % mod
    modulos.append((mod, target))

# Part A
start_time = timer()
print(chinese_remainder(modulos))
end_time = timer()
#print("Took {} seconds.\n".format(end_time - start_time))

# Part B
modulos.append((11, 11 - len(modulos) - 1))
start_time = timer()
print(chinese_remainder(modulos))
end_time = timer()
#print("Took {} seconds.\n".format(end_time - start_time))


# Brute Force Solution
def solve_old():
    start_time = timer()
    current_time = 0
    while True:
        for m, a in modulos:
            if current_time % m != a:
                break
        else:
            break
        current_time += 1

    print(current_time)
    end_time = timer()
    print("Took {} seconds.\n".format(end_time - start_time))
