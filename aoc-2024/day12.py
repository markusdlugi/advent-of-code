from collections import defaultdict

lines = [line.strip() for line in open("input/12.txt")]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
regions = defaultdict(list)
counter = defaultdict(int)
for r, line in enumerate(lines):
    for c, word in enumerate(line):
        current_key = word + str(counter[word])
        connected = False
        for d in range(4):
            rr, cc = r + dr[d], c + dc[d]
            if 0 <= rr < len(lines) and 0 <= cc < len(lines[r]) and lines[rr][cc] == word:
                for name, region in regions.items():
                    if (rr, cc) in region:
                        connected = True
                        current_key = name
                        break
        if not connected:
            counter[word] += 1
            current_key = word + str(counter[word])

        regions[current_key].append((r, c))

to_join = []
for name, region in regions.items():
    for name2, region2 in regions.items():
        if name != name2 and name[0] == name2[0]:
            join = False
            for r, c in region:
                for d in range(4):
                    rr, cc = r + dr[d], c + dc[d]
                    if 0 <= rr < len(lines) and 0 <= cc < len(lines[r]) and (rr, cc) in region2:
                        join = True
                        break
                if join:
                    break
            if join:
                to_join.append((name, name2))

for a, b in to_join:
    regions[a].extend(regions[b])
    del regions[b]

to_join = []
for name, region in regions.items():
    for name2, region2 in regions.items():
        if name != name2 and name[0] == name2[0]:
            join = False
            for r, c in region:
                for d in range(4):
                    rr, cc = r + dr[d], c + dc[d]
                    if 0 <= rr < len(lines) and 0 <= cc < len(lines[r]) and (rr, cc) in region2:
                        join = True
                        break
                if join:
                    break
            if join:
                to_join.append((name, name2))

for a, b in to_join:
    regions[a].extend(regions[b])
    del regions[b]

to_join = []
for name, region in regions.items():
    for name2, region2 in regions.items():
        if name != name2 and name[0] == name2[0]:
            join = False
            for r, c in region:
                for d in range(4):
                    rr, cc = r + dr[d], c + dc[d]
                    if 0 <= rr < len(lines) and 0 <= cc < len(lines[r]) and (rr, cc) in region2:
                        join = True
                        break
                if join:
                    break
            if join:
                to_join.append((name, name2))

for a, b in to_join:
    regions[a].extend(regions[b])
    del regions[b]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
total_price = 0
for name, region in regions.items():
    area = len(region)
    fence = 0
    side_map = defaultdict(list)
    start = None
    for (r, c) in region:
        for d in range(4):
            rr, cc = r + dr[d], c + dc[d]
            if not (0 <= rr < len(lines) and 0 <= cc < len(lines[r])):
                fence += 1
                side_map[d].append((r, c))
                if start is None:
                    start = (r, c, d)
            elif (rr, cc) not in region:
                fence += 1
                side_map[d].append((r, c))
                if start is None:
                    start = (r, c, d)

    for d, sides in side_map.items():
        for r, c in sides:
            to_remove = []
            for rr, cc in sides:
                if r == rr and c == cc:
                    continue
                if r != rr and c != cc:
                    continue
                adjacent = False
                if c == cc:
                    for rrr in range(min(r, rr), max(r, rr)):
                        neighbor = rrr + dr[d], c + dc[d]
                        if (rrr, c) not in region or neighbor in region:
                            break
                    else:
                        adjacent = True
                else:
                    for ccc in range(min(c, cc), max(c, cc)):
                        neighbor = r + dr[d], ccc + dc[d]
                        if (r, ccc) not in region or neighbor in region:
                            break
                    else:
                        adjacent = True
                if adjacent:
                    to_remove.append((rr, cc))
            for side in to_remove:
                sides.remove(side)

    sum_sides = 0
    for side in side_map.values():
        sum_sides += len(side)

    price = area * sum_sides
    print(f"{name}: {area} * {sum_sides} = {price}")
    total_price += price

print(total_price)
