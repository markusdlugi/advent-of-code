directions = open("input/01.txt").read().strip().split(", ")

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

start = (0, 0)
current = start
d = 0
visited = set()
twice = None
for direction in directions:
    if direction[0] == "L":
        d = (d + 3) % 4
    elif direction[0] == "R":
        d = (d + 1) % 4
    else:
        assert False

    for i in range(int(direction[1:])):
        current = (current[0] + dx[d], current[1] + dy[d])
        if twice is None and current in visited:
            twice = current
        visited.add(current)

print(abs(current[0]) + abs(current[1]))
print(abs(twice[0]) + abs(twice[1]))
