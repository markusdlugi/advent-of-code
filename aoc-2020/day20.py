from collections import Counter, defaultdict, deque
from itertools import product
from timeit import default_timer as timer
import math

start = timer()
with open("input/20.txt") as field:
    tiles = [section.splitlines() for section in field.read().split("\n\n")]

tilemap = {}
for tile in tiles:
    n = int(tile[0].split()[1][:-1])
    lines = tile[1:]

    map_ = {}
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            map_[(x, y)] = ch
    tilemap[n] = map_

width = x + 1
height = y + 1
dx, dy = ((0, 1, 0, -1), (-1, 0, 1, 0))


def get_borders(tilemap, width, height):
    for x in [0, width - 1]:
        yield "".join(tilemap[(x, y)] for y in range(0, height))
    for y in [0, height - 1]:
        yield "".join(tilemap[(x, y)] for x in range(0, width))


def flip(flip_x, flip_y, tilemap, width, height):
    result = {}
    for coord, ch in tilemap.items():
        x, y = coord
        new_x = width - 1 - x if flip_x else x
        new_y = height - 1 - y if flip_y else y
        result[(new_x, new_y)] = ch
    return result


def rot(clockwise, tilemap, width, height):
    result = {}
    for coord, ch in tilemap.items():
        x, y = coord
        new_x = y if clockwise else (-y - 1) % height
        new_y = (-x - 1) % width if clockwise else x
        result[(new_x, new_y)] = ch
    return result


def aligns(a, b):
    border_range = {0: (range(width), [0]), 1: ([width - 1], range(height)), 2: (range(width), [height - 1]),
                    3: ([0], range(height))}
    for border in range(4):
        rx, ry = border_range[border]
        align = True
        for x in rx:
            for y in ry:
                if a[(x, y)] != b[((x + dx[border]) % width, (y + dy[border]) % height)]:
                    align = False
                    break
            if not align:
                break
        if align:
            return border
    return -1


def get_transformations(tmap, width, height):
    for flip_x, flip_y in product([True, False], [True, False]):
        yield flip(flip_x, flip_y, tmap, width, height)
    for cw in [True, False]:
        rotated = rot(cw, tmap, width, height)
        yield rotated
        yield flip(True, False, rotated, width, height)


# Part A
# Get borders of all tiles
bordermap = defaultdict(list)
for tid, tmap in tilemap.items():
    for border in get_borders(tmap, width, height):
        bordermap[border].append(tid)
        bordermap[border[::-1]].append(tid)

# Build neighbor map
neighbors = defaultdict(set)
for tiles in bordermap.values():
    for tile in tiles:
        neighbors[tile].update(tiles)
        neighbors[tile].remove(tile)

# Get corners (only 2 neighbors)
start_tile = None
prod_ = 1
for i, n in neighbors.items():
    if len(n) == 2:
        prod_ *= i
        if start_tile is None:
            start_tile = i
print(prod_)


# Part B
# Find correct position and orientation of all tiles
arranged = {start_tile: (0, 0)}

q = deque([(start_tile, n) for n in neighbors[start_tile]])
while q:
    a, b = q.popleft()
    if b in arranged:
        continue
    for b_map in get_transformations(tilemap[b], width, height):
        border = aligns(tilemap[a], b_map)
        if border != -1:
            x, y = (arranged[a][0] + dx[border], arranged[a][1] + dy[border])
            arranged[b] = (x, y)
            tilemap[b] = b_map
            q.extend([(b, n) for n in neighbors[b] if n not in arranged])
            break

# Build inverse and find dimensions of map
arr_inv = {v: k for k, v in arranged.items()}
minx = min(arr_inv.keys(), key=lambda x: x[0])[0]
miny = min(arr_inv.keys(), key=lambda x: x[1])[1]
maxx = max(arr_inv.keys(), key=lambda x: x[0])[0]
maxy = max(arr_inv.keys(), key=lambda x: x[1])[1]

# Fill new dict with chars from all tiles
seamap = {}
for r, y in enumerate(range(miny, maxy + 1)):
    for c, x in enumerate(range(minx, maxx + 1)):
        tile = arr_inv[(x, y)]
        # Remove borders by reducing range
        for yy in range(1, height - 1):
            for xx in range(1, width - 1):
                new_x, new_y = (c * (width - 2) + (xx - 1), r * (height - 2) + (yy - 1))
                seamap[(new_x, new_y)] = tilemap[tile][(xx, yy)]

# New image height and weight
width = height = int(math.sqrt(len(tilemap))) * (width - 2)

## Seamonster looks like this:
##                   #
## #    ##    ##    ###
##  #  #  #  #  #  #
seamonster = [(0, 0), (1, 1), (4, 1), (5, 0), (6, 0), (7, 1), (10, 1), (11, 0), (12, 0), (13, 1), (16, 1), (17, 0),
              (18, 0), (18, -1), (19, 0)]


def is_seamonster(x, y, seamap):
    exists = True
    for (dx, dy) in seamonster:
        xx, yy = (x + dx, y + dy)
        if (xx, yy) not in seamap or seamap[(xx, yy)] != "#":
            exists = False
            break
    if exists:
        for (dx, dy) in seamonster:
            xx, yy = (x + dx, y + dy)
            seamap[(xx, yy)] = "O"
    return exists


# Find seamonsters!
seamonster_count = 0
for map_ in get_transformations(seamap, width, height):
    seamonster_count = sum(1 for y in range(height) for x in range(width) if is_seamonster(x, y, map_))
    if seamonster_count > 0:
        break

#for y in range(height):
#    print("".join(m[(x, y)] for x in range(width)))

hash_count = Counter(seamap.values())["#"]
seamonster_hashes = seamonster_count * len(seamonster)
print(hash_count - seamonster_hashes)

end = timer()
print(f'Took {round((end - start) * 1000, 2)} ms.')
