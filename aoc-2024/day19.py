from functools import lru_cache


@lru_cache(100000)
def arrangement_count(design: str):
    if len(design) == 0:
        return 1

    return sum(arrangement_count(design[len(pattern):]) if design.startswith(pattern) else 0 for pattern in patterns)


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/19.txt")]
    patterns = lines[0].split(", ")
    designs = lines[2:]

    arrangements = [arrangement_count(design) for design in designs]

    possible = sum(1 if arrangement > 0 else 0 for arrangement in arrangements)
    print(possible)
    
    total_count = sum(arrangements)
    print(total_count)
