from collections import deque
from itertools import combinations

numbers = list(map(int, open("input/09.txt")))

# Part A
target = 0
window = deque()
for n in numbers:
    if len(window) < 25:
        window.append(n)
        continue
    valid = False
    for a, b in combinations(window, 2):
        if a + b == n:
            valid = True
            break
    if not valid:
        target = n
        break
    window.append(n)
    window.popleft()
print(target)

# Part B
window = deque()
for n in numbers:
    window.append(n)
    sum_ = sum(window)
    while sum_ > target:
        sum_ -= window.popleft()
    if sum_ == target:
        print(min(window) + max(window))
        break
