text = open("input/01.txt").read()

floor = 0
current_pos = 0
first_pos = None

for char in text:
    current_pos += 1
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if first_pos is None and floor == -1:
        first_pos = current_pos

print(floor)
print(first_pos)
