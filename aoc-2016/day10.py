import re
from collections import defaultdict

input_low, input_high = 17, 61

value_pattern = r'value (\d+) goes to bot (\d+)'
giving_pattern = r'bot (\d+) gives low to ([a-z]+) (\d+) and high to ([a-z]+) (\d+)'
file = open("input/10.txt").read()

bots = defaultdict(list)
values = list(map(lambda x: (int(x[0]), int(x[1])), re.findall(value_pattern, file)))
for value, bot in values:
    bots[bot].append(value)

giving = dict()
rules = list(map(lambda x: (int(x[0]), x[1], int(x[2]), x[3], int(x[4])), re.findall(giving_pattern, file)))
for bot, low_target, low_target_no, high_target, high_target_no in rules:
    giving[bot] = (low_target, low_target_no, high_target, high_target_no)

outputs = defaultdict(list)
targets = {"bot": bots, "output": outputs}
while sum(len(x) for x in bots.values()) > 0:
    for k, v in bots.copy().items():
        if len(v) < 2:
            continue
        low, high = min(v), max(v)
        if low == input_low and high == input_high:
            print(k)
        bots[k].clear()

        low_target, low_no, high_target, high_no = (giving[k][x] for x in range(4))
        targets[low_target][low_no].append(low)
        targets[high_target][high_no].append(high)

a, b, c = (outputs[k][0] for k in [0, 1, 2])
print(a * b * c)
