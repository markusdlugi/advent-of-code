from collections import defaultdict

path_cache = defaultdict(int)


def paths(numbers, choices, i):
    global path_cache
    if i == max(numbers):
        return 1
    if i in path_cache:
        return path_cache[i]
    result = 0
    for c in choices[i]:
        result += paths(numbers, choices, i + c)
    path_cache[i] = result
    return result


numbers = list(map(int, open("input/10.txt")))
numbers.append(0)
numbers.append(max(numbers) + 3)
numbers.sort()

# Part A
diff = defaultdict(int)
prev = None
choices = defaultdict(list)
for num in numbers:
    choices[num].extend((i for i in range(1, 4) if num + i in numbers))

    if prev is not None:
        diff[num - prev] += 1
    prev = num

print(diff[1] * diff[3])

# Part B
print(paths(numbers, choices, 0))
