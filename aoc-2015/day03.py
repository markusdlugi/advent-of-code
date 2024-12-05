instructions = open("input/03.txt").read()

directions = ['^', '>', 'v', '<']
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# Part A
pos = (0, 0)
houses = set()
houses.add(pos)
for char in instructions:
    d = directions.index(char)
    pos = (pos[0] + dx[d], pos[1] + dy[d])
    houses.add(pos)
print(len(houses))

# Part B
santa_pos = (0, 0)
robo_pos = (0, 0)
houses.clear()
houses.add(santa_pos)
for i, char in enumerate(instructions):
    d = directions.index(char)
    if i % 2 == 0:
        santa_pos = (santa_pos[0] + dx[d], santa_pos[1] + dy[d])
        houses.add(santa_pos)
    else:
        robo_pos = (robo_pos[0] + dx[d], robo_pos[1] + dy[d])
        houses.add(robo_pos)

print(len(houses))
