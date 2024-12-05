import re

lines = list(open("input/03.txt"))

result_part1 = 0
result_part2 = 0
enabled = True
for line in lines:
    for match in re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", line):
        if "do()" == match[0]:
            enabled = True
        elif "don't()" == match[0]:
            enabled = False
        else:
            a, b = int(match[1]), int(match[2])
            result_part1 += a * b
            if enabled:
                result_part2 += a * b

print(result_part1)
print(result_part2)
