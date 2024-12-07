import math


def solve(result: int, current: int, numbers: list, operators: str):
    if not numbers:
        return current == result
    if current < 0:
        return False

    next_number = numbers[-1]
    remaining = numbers[:-1]

    for operator in operators:
        if operator == '|':
            digits = int(math.log10(next_number)) + 1
            end_removed = math.floor(current * 10 ** (digits * -1))
            if end_removed * 10 ** digits + next_number != current:
                continue
            if solve(result, end_removed, remaining, operators):
                return True
        elif operator == '+':
            if solve(result, current - next_number, remaining, operators):
                return True
        elif operator == '*':
            if current % next_number != 0:
                continue
            if solve(result, int(current / next_number), remaining, operators):
                return True


def is_solvable(result: int, numbers: list, operators: str):
    return solve(numbers[0], result, numbers[1:], operators)


def part1(equations: list):
    sum_part1 = 0
    part1_valid = set()
    for result, numbers in equations:
        if is_solvable(result, numbers, '+*'):
            sum_part1 += result
            part1_valid.add(result)

    print(f"{sum_part1}")

    return (sum_part1, part1_valid)


def part2(equations: list, sum_part1: int, part1_valid: set):
    sum_part2 = 0
    for result, numbers in equations:
        if result in part1_valid:
            continue
        if is_solvable(result, numbers, '+*|'):
            sum_part2 += result

    print(f"{sum_part1 + sum_part2}")


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/07.txt")]

    equations = []
    for line in lines:
        result, rest = line.split(':')
        result = int(result)
        numbers = list(map(int, rest.strip().split(' ')))
        equations.append((result, numbers))

    sum_part1, part1_valid = part1(equations)
    part2(equations, sum_part1, part1_valid)
