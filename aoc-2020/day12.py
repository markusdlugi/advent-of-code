import math
from collections import namedtuple

lines = [line.strip() for line in open("input/12.txt")]

Position = namedtuple("Position", "x y")
dx, dy = ((0, 1, 0, -1), (-1, 0, 1, 0))
NESW = {"N": 0, "E": 1, "S": 2, "W": 3}
FRL = {"F": 0, "R": 1, "L": 3}

# Part A
pos = Position(0, 0)
dir_ = 1
for line in lines:
    d, steps = line[0], int(line[1:])
    if d in NESW:
        pos = Position(pos.x + steps * dx[NESW[d]], pos.y + steps * dy[NESW[d]])
    else:
        if d == "F":
            pos = Position(pos.x + steps * dx[dir_], pos.y + steps * dy[dir_])
        else:
            dir_ = (dir_ + FRL[d] * (steps // 90)) % 4
print(abs(pos.x) + abs(pos.y))

# Part B
waypoint = Position(10, -1)
ship = Position(0, 0)
for line in lines:
    d, steps = line[0], int(line[1:])
    if d in NESW:
        waypoint = Position(waypoint.x + steps * dx[NESW[d]], waypoint.y + steps * dy[NESW[d]])
    else:
        if d == "F":
            ship = Position(ship.x + steps * waypoint.x, ship.y + steps * waypoint.y)
        else:
            rad = math.radians(steps if d == "R" else (360 - steps))
            s = math.sin(rad)
            c = math.cos(rad)

            waypoint = Position(c * waypoint.x - s * waypoint.y, s * waypoint.x + c * waypoint.y)
print(int(round(abs(ship.x) + abs(ship.y), 0)))
