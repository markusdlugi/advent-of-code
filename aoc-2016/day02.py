def get_code(lines, keypad, start):
    curr = start
    result = []
    d = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
    for line in lines:
        for char in line:
            prev = curr
            curr = (max(0, min(len(keypad)-1, curr[0] + d[char][0])),
                    max(0, min(len(keypad[0])-1, curr[1] + d[char][1])))
            if keypad[curr[0]][curr[1]] == 0:
                curr = prev

        result.append(keypad[curr[0]][curr[1]])
    return result


keypad1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
keypad2 = ((0, 0, 1, 0, 0), (0, 2, 3, 4, 0), (5, 6, 7, 8, 9), (0, "A", "B", "C", 0), (0, 0, "D", 0, 0))
lines = list(map(lambda l: l.strip(), open("input/02.txt")))

print(*get_code(lines, keypad1, (1, 1)), sep='')
print(*get_code(lines, keypad2, (2, 0)), sep='')
