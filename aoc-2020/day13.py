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

    return x % M


lines = [line.strip() for line in open("input/13.txt")]

depart = int(lines[0])
times = lines[1].split(",")
ids = [int(x) for x in times if x != "x"]

# Part A
t = depart
found = None
while not found:
    t += 1
    found = [id for id in ids if t % id == 0]

print((t - depart) * found[0])

# Part B
modulos = []
for i, m in enumerate(times):
    if m == 'x':
        continue
    modulos.append((int(m), int(m) - i))

print(chinese_remainder(modulos))
