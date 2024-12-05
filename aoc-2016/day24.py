from collections import deque
from itertools import combinations
from itertools import permutations


def bfs(start, end, grid):
    start_state = (0, start)
    visited, queue = {start}, deque([start_state])

    while queue:
        curr = queue.popleft()
        if curr[1] == end:
            return curr[0]
        for m in moves(curr, grid):
            if m[1] not in visited:
                visited.add(m[1])
                queue.append(m)


def moves(state, grid):
    steps, pos = state
    steps += 1
    result = []
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
    for d in range(4):
        new_pos = (pos[0] + dx[d], pos[1] + dy[d])
        if not 0 <= new_pos[0] <= len(grid[0]) or not 0 <= new_pos[1] <= len(grid):
            continue
        if grid[new_pos[1]][new_pos[0]]:
            continue
        result.append((steps, new_pos))
    return result


def shortest_route(keys, dist, start, return_to_start):
    min_steps = None
    for perm in permutations(keys):
        steps = 0
        curr = start
        for key in perm:
            steps += dist[(curr, key)]
            curr = key
        if return_to_start:
            steps += dist[(curr, start)]
        min_steps = steps if min_steps is None else min(min_steps, steps)
    return min_steps


# Build grid from input
grid = []
start = None
keys = []
for y, line in enumerate(open("input/24.txt")):
    line = line.strip()
    positions = []
    for x, char in enumerate(line):
        if char == "#":
            positions.append(1)
        elif char == ".":
            positions.append(0)
        elif char.isdigit():
            if char == "0":
                start = (x, y)
            keys.append((x, y))
            positions.append(0)
    grid.append(positions)

# Calculate all distances between pairs
dist = {}
for pair in combinations(keys, 2):
    shortest_distance = bfs(pair[0], pair[1], grid)
    dist[pair] = dist[(pair[1], pair[0])] = shortest_distance
keys.remove(start)

# Part A
print(shortest_route(keys, dist, start, False))
# Part B
print(shortest_route(keys, dist, start, True))
