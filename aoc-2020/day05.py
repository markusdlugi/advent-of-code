import re

lines = [line.strip() for line in open("input/05.txt")]


# First solution with binary search -.-
def solve_old():
    rows = 128
    cols = 8

    seats = []
    for line in lines:
        row_chars, col_chars = (line[:7], line[7:])

        # Find row
        lo, hi = (0, rows - 1)
        for ch in row_chars:
            if ch == "F":
                hi = (lo + hi) // 2 - 1
            else:
                lo = (lo + hi) // 2 + 1
        r = lo

        # Find col
        lo, hi = (0, cols - 1)
        for ch in col_chars:
            if ch == "L":
                hi = (lo + hi) // 2 - 1
            else:
                lo = (lo + hi) // 2 + 1
        c = lo

        seats.append(8 * r + c)

    max_seat_id = max(seats)
    print(max_seat_id)

    for i in range(max_seat_id):
        if i - 1 in seats and i + 1 in seats and i not in seats:
            print(i)
            break


# Refined solution with converting to binary :)
seats = []
for line in lines:
    line = re.sub(r'[BR]', '1', line)
    line = re.sub(r'[FL]', '0', line)
    seats.append(int(line, 2))
seats.sort()
print(seats[-1])

for i in seats:
    if i + 1 not in seats and i + 2 in seats:
        print(i + 1)
        break
