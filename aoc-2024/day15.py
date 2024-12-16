from collections import deque

lines = [line.strip() for line in open("input/15.txt")]


def print_grid(boxes, wall, pos):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if r == pos[0] and c == pos[1]:
                print("@", end="")
            elif (r, c) in boxes:
                print("[]", end="")
            elif (r, c - 1) in boxes:
                continue
            elif (r, c) in wall:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def next_move(r, c, d, grid, boxes, wall):
    dr, dc = ([-1, 0, 1, 0], [0, 1, 0, -1])
    rr, cc = r + dr[d], c + dc[d]
    if (rr, cc) in wall:
        return r, c
    elif (rr, cc) in boxes or (rr, cc - 1) in boxes:
        to_be_moved = set()
        if (rr, cc) in boxes:
            to_be_moved.add((rr, cc))
            to_be_moved.add((rr, cc + 1))
        else:
            to_be_moved.add((rr, cc - 1))
            to_be_moved.add((rr, cc))
        can_move = True
        continue_loop = True
        while continue_loop:
            continue_loop = False
            next_to_be_moved = set()
            for box_rr, box_cc in to_be_moved:
                rrr, ccc = box_rr + dr[d], box_cc + dc[d]
                while True:
                    if (rrr, ccc) in wall:
                        can_move = False
                        break
                    elif not (rrr, ccc) in boxes and not (rrr, ccc - 1) in boxes:
                        break
                    elif (rrr, ccc) in boxes:
                        if not (rrr, ccc) in to_be_moved:
                            next_to_be_moved.add((rrr, ccc))
                        if not (rrr, ccc + 1) in to_be_moved:
                            next_to_be_moved.add((rrr, ccc + 1))
                    elif (rrr, ccc - 1) in boxes:
                        if not (rrr, ccc - 1) in to_be_moved:
                            next_to_be_moved.add((rrr, ccc - 1))
                        if not (rrr, ccc) in to_be_moved:
                            next_to_be_moved.add((rrr, ccc))
                    rrr, ccc = rrr + dr[d], ccc + dc[d]
            if next_to_be_moved:
                continue_loop = True
                to_be_moved.update(next_to_be_moved)
        if can_move:
            to_remove = set()
            to_add = set()
            for box_rr, box_cc in to_be_moved:
                rrr, ccc = box_rr + dr[d], box_cc + dc[d]
                if (box_rr, box_cc) in boxes:
                    to_remove.add((box_rr, box_cc))
                    to_add.add((rrr, ccc))
            for box_rr, box_cc in to_remove:
                boxes.remove((box_rr, box_cc))
            for box_rr, box_cc in to_add:
                boxes.add((box_rr, box_cc))
            return rr, cc
        else:
            return r, c
    else:
        return rr, cc


grid = []
move_lines = []
for line in lines:
    if line.startswith("#"):
        grid.append(line)
    else:
        move_lines.append(line)

new_grid = []
for r, line in enumerate(grid):
    new_line = ""
    for c, word in enumerate(grid[r]):
        if word == "@":
            new_line = new_line + "@."
        elif word == "#":
            new_line = new_line + "##"
        elif word == "O":
            new_line = new_line + "[]"
        elif word == ".":
            new_line = new_line + ".."
    new_grid.append(new_line)

grid = new_grid

start = None
boxes = set()
wall = set()
for r, line in enumerate(grid):
    for c, word in enumerate(grid[r]):
        if word == "@":
            start = (r, c)
        elif word == "[":
            boxes.add((r, c))
        elif word == "#":
            wall.add((r, c))

m = {"^": 0, ">": 1, "v": 2, "<": 3}
moves = deque()
for move_line in move_lines:
    for move in move_line:
        moves.append(m[move])

q = deque([start])
visited = set()
while moves:
    r, c = q.popleft()
    d = moves.popleft()
    rr, cc = next_move(r, c, d, grid, boxes, wall)
    # print_grid(boxes, wall, (rr, cc))
    q.append((rr, cc))
    visited.add((r, c))

gps = 0
for r, c in boxes:
    gps += 100 * r + c

print(gps)
