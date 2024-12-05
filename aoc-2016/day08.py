import re

width, height = 50, 6
lights = set()

rect_pattern = r'rect (\d+)x(\d+)'
rotate_row_pattern = r'rotate row y=(\d+) by (\d+)'
rotate_col_pattern = r'rotate column x=(\d+) by (\d+)'
for line in open("input/08.txt"):
    line = line.strip()

    if line.startswith("rect"):
        rect_width, rect_height = tuple(map(int, re.findall(rect_pattern, line)[0]))
        for a in range(rect_width):
            for b in range(rect_height):
                lights.add((a, b))
    elif line.startswith("rotate row"):
        row, diff = tuple(map(int, re.findall(rotate_row_pattern, line)[0]))
        old_lights = set()
        new_lights = set()
        for x, y in lights:
            if y == row:
                old_lights.add((x, y))
                x = (x + diff) % width
                new_lights.add((x, y))
        lights.difference_update(old_lights)
        lights.update(new_lights)
    elif line.startswith("rotate col"):
        col, diff = tuple(map(int, re.findall(rotate_col_pattern, line)[0]))
        old_lights = set()
        new_lights = set()
        for x, y in lights:
            if x == col:
                old_lights.add((x, y))
                y = (y + diff) % height
                new_lights.add((x, y))
        lights.difference_update(old_lights)
        lights.update(new_lights)

print(len(lights))
print()

for y in range(height):
    for x in range(width):
        if (x, y) in lights:
            print("#", end='')
        else:
            print(" ", end='')
    print("")
