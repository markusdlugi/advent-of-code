import re
from collections import deque, defaultdict
from functools import lru_cache

lines = [line.strip() for line in open("input/07.txt")]

bags = defaultdict(list)
for line in lines:
    container = re.findall(r'([a-z ]*) bags contain', line)[0]
    bags[container].extend((int(num), bag) for num, bag in re.findall(r'(\d+) ([a-z ]*) bag[s]?[,.]?', line[len(container) + 13:]))

# Part A
found = set()


@lru_cache(maxsize=10000)
def find_shiny_gold(bag):
    if bag == "shiny gold":
        return True
    if any(find_shiny_gold(bag) for (num, bag) in bags[bag]):
        found.add(bag)
        return True
    return False


for bag in list(bags.keys()):
    find_shiny_gold(bag)
print(len(found))


# Part B
def count_bags(bag, count):
    return count + count * sum(count_bags(b, n) for (n, b) in bags[bag])


print(count_bags("shiny gold", 1) - 1)
