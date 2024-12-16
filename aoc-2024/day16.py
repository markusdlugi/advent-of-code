import heapq

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


def shortest_path(grid: list, start: tuple, end: tuple):
    start_r, start_c, start_d = start
    q = [(0, start_r, start_c, start_d, [(start_r, start_c)])]
    visited = {(start_r, start_c, 1): 0}
    end_paths = []
    min_cost = None
    while q:
        cost, r, c, d, path = heapq.heappop(q)
        if (r, c) == end:
            min_cost = cost
            end_paths.append(path)
            continue
        for d_change in range(-1, 2):
            dd = (d + d_change) % 4
            rr, cc = r + dr[dd], c + dc[dd]
            if grid[rr][cc] != "#":
                new_cost = cost + abs(d_change) * 1000 + 1
                if min_cost and new_cost > min_cost:
                    continue
                if (rr, cc, dd) in visited:
                    prev_cost = visited[(rr, cc, dd)]
                    if prev_cost < new_cost:
                        continue
                new_path = path.copy()
                new_path.append((rr, cc))
                visited[(rr, cc, dd)] = new_cost
                heapq.heappush(q, (new_cost, rr, cc, dd, new_path))

    spots = set()
    for path in end_paths:
        spots.update(path)

    return min_cost, len(spots)


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/16.txt")]

    # Start & end should always be in the upper-right and bottom-left corners
    start, end = (len(lines) - 2, 1, 1), (1, len(lines[1]) - 2)
    assert (lines[start[0]][start[1]] == "S")
    assert (lines[end[0]][end[1]] == "E")

    min_score, best_spots = shortest_path(lines, start, end)

    print(min_score)
    print(best_spots)
