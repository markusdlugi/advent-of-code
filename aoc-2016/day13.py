from collections import deque


def is_valid(pos, puzzle_input):
    x, y = pos
    if x < 0 or y < 0:
        return False
    number = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
    bits = bin(number).count("1")
    return bits % 2 == 0


def moves(state, puzzle_input):
    result = []
    steps = state[0] + 1
    x, y = state[1]
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
    for d in range(4):
        new_pos = (x + dx[d], y + dy[d])
        if is_valid(new_pos, puzzle_input):
            result.append((steps, new_pos))
    return result


puzzle_input = 1350
target = (31, 39)
start = (1, 1)

visited, queue = {start}, deque([(0, start)])
location_count = 1
curr = start
while queue:
    curr = queue.popleft()
    if curr[1] == target:
        break
    for m in moves(curr, puzzle_input):
        if m[1] not in visited:
            visited.add(m[1])
            queue.append(m)
            if m[0] <= 50:
                location_count += 1

# Part A
print(curr[0])
# Part B
print(location_count)
