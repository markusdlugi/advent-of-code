from collections import deque, defaultdict


def manhattan(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_shortest_path(walls: set, start: tuple, end: tuple):
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

    q = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1]): 0}
    shortest_path = None
    while q:
        r, c, path = q.popleft()
        if (r, c) == end:
            if shortest_path is None:
                shortest_path = path
            continue
        for d in range(4):
            rr, cc = r + dr[d], c + dc[d]
            if not (0 <= rr < len(lines) and 0 <= cc < len(lines[r])):
                continue

            new_path = path + 1
            if (rr, cc) in visited:
                continue

            if (rr, cc) not in walls:
                visited[(rr, cc)] = new_path
                q.append((rr, cc, new_path))
    return shortest_path, visited


def cheatable_positions(start: tuple, seen: dict, distance: int):
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

    q = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1]): 0}
    while q:
        r, c, path = q.popleft()
        if path >= distance:
            break
        for d in range(4):
            rr, cc = r + dr[d], c + dc[d]

            new_path = path + 1
            if (rr, cc) in visited:
                continue

            visited[(rr, cc)] = new_path
            q.append((rr, cc, new_path))
            if (rr, cc) in seen:
                yield rr, cc


def apply_cheat_rectangle(position: tuple, rectangle: set, visited: dict):
    r, c = position
    for (cr, cc) in rectangle:
        rr, cc = r + cr, c + cc
        if (rr, cc) in visited:
            yield rr, cc


def find_cheats(cheat_distance: int, shortest_path: int, visited: dict):
    result = dict()
    for a in visited:
        for b in cheatable_positions(a, visited, cheat_distance):
            distance = manhattan(a, b)
            if visited[a] > visited[b]:
                cheat_id = (a, b)
                cheat_path_length = (shortest_path - visited[a]) + distance + visited[b]
            else:
                cheat_id = (b, a)
                cheat_path_length = (shortest_path - visited[b]) + distance + visited[a]
            if cheat_path_length < shortest_path:
                result[cheat_id] = shortest_path - cheat_path_length
    return result


def find_best_cheats(cheat_distance: int, shortest_path: int, visited: dict):
    cheats = defaultdict(int)
    cheat_paths = find_cheats(cheat_distance, shortest_path, visited)
    for cheat_id, cheat_saved in cheat_paths.items():
        cheats[cheat_saved] += 1

    return sum(count for saved, count in cheats.items() if saved >= 100)


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/20.txt")]

    start = None
    end = None
    walls = set()
    for r, line in enumerate(lines):
        for c, word in enumerate(line):

            if word == "S":
                start = r, c
            elif word == "E":
                end = r, c
            elif word == "#":
                walls.add((r, c))

    shortest_path, visited = find_shortest_path(walls, end, start)

    print(find_best_cheats(2, shortest_path, visited))
    print(find_best_cheats(20, shortest_path, visited))
