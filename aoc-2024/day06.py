from collections import deque

lines = [line.strip() for line in open("input/06.txt")]
dr, dc = ([-1, 0, 1, 0], [0, 1, 0, -1])


def moves(r, c, d, maze):
    rr, cc = r + dr[d], c + dc[d]
    if not (0 <= rr < len(maze) and 0 <= cc < len(maze[r])):
        return rr, cc, d
    next = maze[rr][cc]
    if next != "#" and next != "O":
        return rr, cc, d
    else:
        return r, c, (d + 1) % 4


start = None
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == "^":
            start = (r, c, 0)
            break
    if start:
        break

positions = set()
visited = set()
q = deque([start])
guard = ["^", ">", "v", "<"]
while q:
    r, c, d = q.popleft()
    if len(positions) > 0 and not (0 <= r < len(lines) and 0 <= c < len(lines[r])):
        break
    positions.add((r, c))
    visited.add((r, c, d))
    # lines[r] = lines[r][:c] + guard[d] + lines[r][c + 1:]
    rr, cc, dd = moves(r, c, d, lines)
    q.append((rr, cc, dd))

print(len(positions))

loops = 0
old_pos = positions.copy()
maze = lines.copy()
wrong_obs = set()
for obstruction_r, obstruction_c in old_pos:
    if (obstruction_r, obstruction_c, 0) == start:
        continue
    maze[obstruction_r] = maze[obstruction_r][:obstruction_c] + "O" + maze[obstruction_r][obstruction_c + 1:]
    visited = set()
    positions = set()
    q = deque([start])
    wrong = False
    while q:
        r, c, d = q.popleft()
        if len(positions) > 0 and not (0 <= r < len(maze) and 0 <= c < len(maze[r])):
            break
        maze[r] = maze[r][:c] + guard[d] + maze[r][c + 1:]
        positions.add((r, c))
        visited.add((r, c, d))
        rr, cc, dd = moves(r, c, d, maze)
        if not (rr, cc, dd) in visited:
            q.append((rr, cc, dd))
        else:
            loops += 1
            break
    maze[obstruction_r] = maze[obstruction_r][:obstruction_c] + "." + maze[obstruction_r][obstruction_c + 1:]

print(loops)
