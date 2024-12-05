import re

command_pattern = r'([a-z ]*)(\d*),(\d*) through (\d*),(\d*)'

# Part A
lights = []
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(0)

for line in open("input/06.txt"):
    match = re.match(command_pattern, line.strip())
    pos = [match.group(1).strip()]
    for i in range(2, 6, 2):
        pos.append((int(match.group(i)), int(match.group(i+1))))
    if pos[0] == 'turn on':
        for x in range(pos[1][0], pos[2][0]+1):
            for y in range(pos[1][1], pos[2][1]+1):
                lights[x][y] = 1
    elif pos[0] == 'turn off':
        for x in range(pos[1][0], pos[2][0] + 1):
            for y in range(pos[1][1], pos[2][1] + 1):
                lights[x][y] = 0
    elif pos[0] == 'toggle':
        for x in range(pos[1][0], pos[2][0] + 1):
            for y in range(pos[1][1], pos[2][1] + 1):
                lights[x][y] = (lights[x][y] + 1) % 2
    else:
        assert False

count = sum(sum(x) for x in lights)
print(count)

# Part B
lights = []
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(0)

for line in open("input/06.txt"):
    match = re.match(command_pattern, line.strip())
    pos = [match.group(1).strip()]
    for i in range(2, 6, 2):
        pos.append((int(match.group(i)), int(match.group(i + 1))))
    if pos[0] == 'turn on':
        for x in range(pos[1][0], pos[2][0] + 1):
            for y in range(pos[1][1], pos[2][1] + 1):
                lights[x][y] += 1
    elif pos[0] == 'turn off':
        for x in range(pos[1][0], pos[2][0] + 1):
            for y in range(pos[1][1], pos[2][1] + 1):
                lights[x][y] = max(lights[x][y] - 1, 0)
    elif pos[0] == 'toggle':
        for x in range(pos[1][0], pos[2][0] + 1):
            for y in range(pos[1][1], pos[2][1] + 1):
                lights[x][y] += 2
    else:
        assert False

count = sum(sum(x) for x in lights)
print(count)
