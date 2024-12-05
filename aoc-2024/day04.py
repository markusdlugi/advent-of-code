from collections import deque

puzzle = [line.strip() for line in open("input/04.txt")]


# First over-engineered solution with BFS
def moves(r, c, d):
    dr, dc = ([-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1])
    for i in range(8) if d is None else [d]:
        rr, cc = r + dr[i], c + dc[i]
        if 0 <= rr < len(puzzle) and 0 <= cc < len(puzzle[r]):
            yield rr, cc, i


def solve_with_bfs():
    found = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if puzzle[r][c] == "X":
                visited = set()
                q = deque([(r, c, None, "X")])
                while q:
                    rr, cc, d, text = q.popleft()
                    if text == "XMAS":
                        found += 1
                        continue
                    if not "XMAS".startswith(text):
                        continue
                    for next_r, next_c, d in moves(rr, cc, d):
                        if (next_r, next_c) not in visited:
                            q.append((next_r, next_c, d, text + puzzle[next_r][next_c]))
                            visited.add((next_r, next_c))
    return found


# Part 1
# Simpler solution just checking all directions and comparing right away
found = 0
dr, dc = ([-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1])
for r in range(len(puzzle)):
    for c in range(len(puzzle[r])):
        if not puzzle[r][c] == "X":
            continue
        for d in range(8):
            for index, char in enumerate("MAS"):
                rr, cc = r + dr[d] * (index + 1), c + dc[d] * (index + 1)
                if not 0 <= rr < len(puzzle) or not 0 <= cc < len(puzzle[rr]) or puzzle[rr][cc] != char:
                    break
            else:
                found += 1
print(found)

# Part 2
found = 0
for r in range(1, len(puzzle) - 1):
    for c in range(1, len(puzzle[r]) - 1):
        if puzzle[r][c] != "A":
            continue
        diagonal1 = puzzle[r - 1][c - 1] + puzzle[r][c] + puzzle[r + 1][c + 1]
        diagonal2 = puzzle[r - 1][c + 1] + puzzle[r][c] + puzzle[r + 1][c - 1]
        if diagonal1 in ["MAS", "SAM"] and diagonal2 in ["MAS", "SAM"]:
            found += 1
print(found)
