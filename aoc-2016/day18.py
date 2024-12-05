from timeit import default_timer as timer
from collections import deque

first_row = open("input/18.txt").read().strip()

start_time = timer()
prev = deque([True if x == "^" else False for x in [".", *list(first_row), "."]])
safe_count = first_row.count(".")
for r in range(400000 - 1):
    row = deque([False])
    tiles = deque([False, prev.popleft(), prev.popleft()])
    for i in range(len(first_row)):
        tiles.popleft()
        tiles.append(prev.popleft())
        trap = tiles[0] ^ tiles[2]
        row.append(trap)
        if not trap:
            safe_count += 1
    row.append(False)
    prev = row

    # Part A
    if r == 40 - 2:
        print(safe_count)

print(safe_count)
end_time = timer()
print("Took {} seconds.".format(end_time - start_time))
