from functools import lru_cache


@lru_cache(100000)
def count_arrangements(design: str):
    if len(design) == 0:
        return 1

    return sum(count_arrangements(design[len(p):]) for p in patterns if design.startswith(p))


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/19.txt")]
    patterns = lines[0].split(", ")
    designs = lines[2:]

    arrangements = [count_arrangements(design) for design in designs]

    possible = sum(1 for a in arrangements if a > 0)
    print(possible)

    total_count = sum(arrangements)
    print(total_count)
