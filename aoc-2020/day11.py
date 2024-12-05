from collections import defaultdict
from copy import deepcopy
from timeit import default_timer as timer

dr, dc = ((-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1))
visible_seats = defaultdict(list)


def in_grid(r, c, R, C):
    return 0 <= r < R and 0 <= c < C


def count_occupied(G, r, c, R, C, new_rules):
    global dr, dc, visible_seats
    sum_ = 0
    if visible_seats[(r, c)]:
        return sum(1 for (rr, cc) in visible_seats[(r, c)] if G[rr][cc] == "#")
    for i in range(8):
        rr, cc = (r + dr[i], c + dc[i])
        while new_rules and in_grid(rr, cc, R, C) and G[rr][cc] == ".":
            rr, cc = (rr + dr[i], cc + dc[i])
        if in_grid(rr, cc, R, C):
            visible_seats[(r, c)].append((rr, cc))
            if G[rr][cc] == "#":
                sum_ += 1
    return sum_


def show(G, R):
    for r in range(0, R):
        print("".join(G[r]))
    print()


def simulate(G, R, C, new_rules):
    changes = True
    while changes:
        changes = False
        new_G = deepcopy(G)

        for r in range(R):
            for c in range(C):
                state = G[r][c]
                if state == ".":
                    continue
                adj_count = count_occupied(G, r, c, R, C, new_rules)
                if state == "L" and adj_count == 0:
                    new_G[r][c] = "#"
                    changes = True
                if state == "#" and adj_count >= (5 if new_rules else 4):
                    new_G[r][c] = "L"
                    changes = True
        G = new_G
        # show(G, R)
    return G


G = [list(line.strip()) for line in open("input/11.txt")]
R, C = (len(G), len(G[0]))

# Part A
start = timer()
OG = deepcopy(G)
G = simulate(G, R, C, False)
print(sum(r.count("#") for r in G))

# Part B
visible_seats.clear()
G = deepcopy(OG)
G = simulate(G, R, C, True)
print(sum(r.count("#") for r in G))

end = timer()
print(f'Took {end - start} seconds.')
