from collections import deque, namedtuple

Region = namedtuple('Region', ['plots', 'neighbors', 'corners'])

# N, E, S, W
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

# NE, SE, SW, NW
corner_dr, corner_dc = [-1, 1, 1, -1], [1, 1, -1, -1]


def count_corners(region: set):
    corners = 0
    for r, c in region:
        for d in range(4):
            corner = r + corner_dr[d], c + corner_dc[d]
            adjacent_in_region = [(r + dr[dd], c + dc[dd]) in region for dd in [d, (d + 1) % 4]]
            if not any(adjacent_in_region) or (all(adjacent_in_region) and not corner in region):
                corners += 1

    return corners


def discover_region(grid: list, start: tuple, plant):
    q = deque([start])
    visited = {start}
    neighbors = 0
    while q:
        r, c = q.popleft()
        for d in range(4):
            rr, cc = r + dr[d], c + dc[d]
            if (rr, cc) in visited:
                continue
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[r]) and grid[rr][cc] == plant:
                visited.add((rr, cc))
                q.append((rr, cc))
            else:
                neighbors += 1

    corners = count_corners(visited)

    return Region(visited, neighbors, corners)


def discover_all_regions(grid: list):
    regions = []
    visited = set()
    for r, line in enumerate(grid):
        for c, plant in enumerate(grid[r]):
            if (r, c) in visited:
                continue
            region = discover_region(grid, (r, c), plant)
            regions.append(region)
            visited.update(region.plots)
    return regions


def calculate_price(regions):
    total_price1 = sum(len(region.plots) * region.neighbors for region in regions)
    print(total_price1)

    total_price2 = sum(len(region.plots) * region.corners for region in regions)
    print(total_price2)


if __name__ == '__main__':
    grid = [line.strip() for line in open("input/12.txt")]

    regions = discover_all_regions(grid)
    calculate_price(regions)
