dx = (0, 1, 1, 1, 0, -1, -1, -1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)


def count_neighbors(x, y, lights):
    sum = 0
    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (new_x, new_y) in lights:
            sum += 1
    return sum


def animate(lights, size, steps, fixed):
    result = lights.copy()
    for step in range(steps):
        result_copy = result.copy()
        for x in range(size):
            for y in range(size):
                if fixed is not None and x in fixed and y in fixed:
                    continue
                count = count_neighbors(x, y, result)
                if (x, y) in result and (count < 2 or count > 3):
                    result_copy.remove((x, y))
                elif (x, y) not in result and count == 3:
                    result_copy.add((x, y))
        result = result_copy
    return result


lights = set()
size = 100
steps = 100
for y, line in enumerate(open("input/18.txt")):
    for x, character in enumerate(line.strip()):
        if character == "#":
            lights.add((x, y))

# Part A
result = animate(lights, size, steps, None)
print(len(result))

# Part B
fixed = [0, size-1]
for x in fixed:
    for y in fixed:
        lights.add((x, y))

result2 = animate(lights, size, steps, fixed)
print(len(result2))
