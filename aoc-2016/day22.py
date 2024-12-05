import re
from itertools import combinations
import heapq
from timeit import default_timer as timer


def get_cost(steps, pos, goal):
    ax, ay = pos
    bx, by = goal
    return steps + abs(ax - bx) + abs(ay - by)


def neighbours(pos):
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
    result = []
    for d in range(4):
        xx, yy = pos[0] + dx[d], pos[1] + dy[d]
        if 0 <= xx <= max_xy[0] and 0 <= yy <= max_xy[1]:
            result.append((xx, yy))
    return result


def moves(state, goal, disks):
    _, steps, pos = state
    steps += 1
    result = []
    for new_pos in neighbours(pos):
        # If used greater than current size of empty disk
        if disks[new_pos][1] > disks[pos][0]:
            continue

        result.append((get_cost(steps, new_pos, goal), steps, new_pos))
    return result


disks = {}
max_xy = (0, 0)
for line in open("input/22.txt"):
    if line.startswith("root") or line.startswith("Filesystem"):
        continue
    x, y = tuple(map(int, re.findall(r'(?:x|y)(\d+)', line)))
    size, used, _ = tuple(map(int, re.findall(r'(\d+)T', line)))
    disks[(x, y)] = (size, used)
    max_xy = (max(max_xy[0], x), max(max_xy[1], y))

# Part A
start_time = timer()
pairs = 0
for disk_a, disk_b in combinations(disks, 2):
    size_a, used_a = disks[disk_a]
    size_b, used_b = disks[disk_b]
    if used_a != 0 and size_b - used_b >= used_a:
        pairs += 1
    if used_b != 0 and size_a - used_a >= used_b:
        pairs += 1
print(pairs)
end_time = timer()
#print("Took {} seconds".format((end_time - start_time)))


# Part B
start_time = timer()
# Find empty disk
for k, v in disks.items():
    if v[1] == 0:
        start = k
        break
# Find shortest path from empty disk to disk in front of goal data
goal = (max_xy[0] - 1, 0)
start_state = (get_cost(0, start, goal), 0, start)
visited, queue = {start}, []
heapq.heappush(queue, start_state)

# A*
steps = 0
while queue:
    curr = heapq.heappop(queue)
    if curr[2] == goal:
        steps = curr[1]
        break
    for m in moves(curr, goal, disks):
        if m[2] not in visited:
            visited.add(m[2])
            heapq.heappush(queue, m)

x_dist = max_xy[0] - 1
print(steps + (x_dist * 5) + 1)
end_time = timer()
#print("Took {} seconds".format((end_time - start_time)))
