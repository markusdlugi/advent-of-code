import itertools

v = set()
e = dict()
for line in open("input/09.txt"):
    first_split = line.strip().split(" to ")
    second_split = first_split[1].split(" = ")
    v.add(first_split[0])
    v.add(second_split[0])
    e[(first_split[0], second_split[0])] = int(second_split[1])
    e[(second_split[0], first_split[0])] = int(second_split[1])

min_distance = None
max_distance = None
for perm in itertools.permutations(v):
    distance = 0
    prev = None
    for curr in perm:
        if prev is not None:
            distance += e[(prev, curr)]
        prev = curr
    if min_distance is None or distance < min_distance:
        min_distance = distance
    if max_distance is None or distance > max_distance:
        max_distance = distance

print(min_distance)
print(max_distance)
