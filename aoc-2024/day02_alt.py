from itertools import tee


def pairwise(iterable):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def is_safe(levels):
    increasing = all(a < b for a, b in pairwise(levels))
    decreasing = all(a > b for a, b in pairwise(levels))
    safe_diff = all(1 <= abs(a - b) <= 3 for a, b in pairwise(levels))
    return (increasing or decreasing) and safe_diff


lines = list(open("input/02.txt"))

reports = [list(map(int, line.split())) for line in lines]
result = sum(is_safe(levels) for levels in reports)

print(result)

result = 0
for levels in reports:
    for removed in range(0, len(levels)):
        dampened_levels = levels.copy()
        del dampened_levels[removed]
        if is_safe(dampened_levels):
            result += 1
            break

print(result)
