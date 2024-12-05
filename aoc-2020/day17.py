from timeit import default_timer as timer

start = timer()
lines = [line.strip() for line in open("input/17.txt")]

G = set()

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            G.add((x, y, 0, 0))

min_ = [0, 0, 0, 0]
max_ = [x, y, 0, 0]


def get_neighbors(pos, fourth_dimension):
    x, y, z, w = pos
    neighbor = [-1, 0, 1]
    for xx in neighbor:
        for yy in neighbor:
            for zz in neighbor:
                for ww in neighbor if fourth_dimension else [0]:
                    if xx == 0 and yy == 0 and zz == 0 and ww == 0:
                        continue
                    yield x + xx, y + yy, z + zz, w + ww


def count_active(G, pos, fourth_dimension):
    sum_ = 0
    for neighbor in get_neighbors(pos, fourth_dimension):
        if neighbor in G:
            sum_ += 1
    return sum_


def simulate(G, fourth_dimension):
    global min_, max_
    for i in range(6):
        new_G = G.copy()

        changeset = set()
        for pos in G:
            changeset.add(pos)
            changeset.update(get_neighbors(pos, fourth_dimension))

        for pos in changeset:
            state = "#" if pos in G else "."
            adj_count = count_active(G, pos, fourth_dimension)
            if state == "#" and (adj_count > 3 or adj_count < 2):
                new_G.remove(pos)
            if state == "." and adj_count == 3:
                new_G.add(pos)
        G = new_G
    return G


OG = G.copy()
G = simulate(G, False)
print(len(G))

G = OG.copy()
G = simulate(G, True)
print(len(G))

end = timer()
print(f'Took {end - start} seconds.')
