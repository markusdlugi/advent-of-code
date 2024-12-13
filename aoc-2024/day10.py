from collections import deque, defaultdict

grid = [line.strip() for line in open("input/10.txt")]


def moves(r, c, h, grid):
    dr, dc = ([-1, 0, 1, 0], [0, 1, 0, -1])
    for d in range(4):
        rr, cc = r + dr[d], c + dc[d]
        if 0 <= rr < len(grid) and 0 <= cc < len(grid[r]) and int(grid[rr][cc]) == h + 1:
            yield rr, cc, int(grid[rr][cc])


def bfs(start):
    trails = list()
    q = deque([start])
    visited = set()
    while q:
        r, c, h = q.popleft()
        visited.add((r, c, h))
        if h == 9:
            end = (r, c, 9)
            trails.append(end)
            continue
        for rr, cc, hh in moves(r, c, h, grid):
            if not (rr, cc, hh) in visited:
                q.append((rr, cc, hh))
    return trails


trail_map = defaultdict(list)
for r, line in enumerate(grid):
    for c, word in enumerate(line):
        if int(word) != 0:
            continue
        start = (r, c, 0)
        trail_map[start] = bfs(start)

print(sum(len(set(trails)) for trails in trail_map.values()))
print(sum(len(trails) for trails in trail_map.values()))
