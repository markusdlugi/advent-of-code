from collections import deque

lines = [line.strip() for line in open("input/18.txt")]


def find_shortest_path(fallen_bytes: list):
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    width = 71
    height = 71
    start = (0, 0)
    exit = (70, 70)

    q = deque([(start[0], start[1], [start])])
    visited = {start: 0}
    while q:
        r, c, path = q.popleft()
        if (r, c) == exit:
            return path
        for d in range(4):
            rr, cc = r + dr[d], c + dc[d]
            new_path = path.copy()
            new_path.append((rr, cc))
            if (rr, cc) in visited:
                if visited[(rr, cc)] < len(new_path):
                    continue
            if 0 <= rr < height and 0 <= cc < width and (rr, cc) not in fallen_bytes:
                visited[(rr, cc)] = len(path)
                q.append((rr, cc, new_path))
    return None


if __name__ == '__main__':
    bytes = []
    for line in lines:
        c, r = tuple(map(int, line.split(",")))
        bytes.append((r, c))

    print(len(find_shortest_path(bytes[:1024])))

    lo, hi = 1025, len(bytes)
    no_path = []
    while hi - lo > 1:
        middle = (hi + lo) // 2
        path = find_shortest_path(bytes[:middle])
        if path:
            lo = middle
        else:
            no_path.append(middle)
            hi = middle
    final_byte = bytes[min(no_path) - 1]
    print(f"{final_byte[1]},{final_byte[0]}")
