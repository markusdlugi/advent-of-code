from collections import deque
import hashlib

puzzle_input = "veumntbg"
dirs = ("U", "D", "L", "R")
dx, dy = {"U": 0, "R": 1, "D": 0, "L": -1}, {"U": -1, "R": 0, "D": 1, "L": 0}


def moves(state):
    pos, path = state
    code = "".join([puzzle_input, *path])
    digest = hashlib.md5(code.encode('utf-8')).hexdigest()[:4]
    result = []
    for i, d in enumerate(dirs):
        if int(digest[i], 16) <= 10:
            continue
        new_pos = (pos[0] + dx[d], pos[1] + dy[d])
        if not 0 <= new_pos[0] <= 3 or not 0 <= new_pos[1] <= 3:
            continue
        new_path = list(path).copy()
        new_path.append(d)
        result.append((new_pos, tuple(new_path)))
    return result


start = (0, 0)
end = (3, 3)

start_state = (start, ())
visited, queue = set(start_state), deque([start_state])
shortest_path = None
longest_path = 0
while queue:
    curr = queue.popleft()
    if curr[0] == end:
        if shortest_path is None:
            shortest_path = "".join(curr[1])
        longest_path = max(longest_path, len(curr[1]))
        continue
    for m in moves(curr):
        if m not in visited:
            visited.add(m)
            queue.append(m)

print(shortest_path)
print(longest_path)
