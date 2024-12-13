import math
from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=100000)
def get_next_numbers(number: int):
    digits = int(math.log10(number)) + 1 if number != 0 else 1
    if number == 0:
        return [1]
    elif digits % 2 == 0:
        left = number // 10 ** (digits // 2)
        right = number - left * 10 ** (digits // 2)
        return [left, right]
    else:
        return [number * 2024]


def blink(numbers: dict, blinks: int):
    for it in range(blinks):
        next_numbers = defaultdict(int)
        for num, count in numbers.items():
            for new in get_next_numbers(num):
                next_numbers[new] += count
            numbers[num] -= count
        numbers = next_numbers
    return numbers


if __name__ == '__main__':
    input_numbers = list(map(int, open("input/11.txt").readline().strip().split()))

    numbers = defaultdict(int)
    for num in input_numbers:
        numbers[num] = 1

    numbers = blink(numbers, 25)
    print(sum(occurence for occurence in numbers.values()))

    numbers = blink(numbers, 50)
    print(sum(occurence for occurence in numbers.values()))
