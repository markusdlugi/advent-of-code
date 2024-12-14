import re
from collections import namedtuple, defaultdict
from functools import reduce
from math import floor
from operator import mul

lines = [line.strip() for line in open("input/14.txt")]

Robot = namedtuple('Robot', ['px', 'py', 'vx', 'vy'])
width = 101
height = 103


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    d, s, t = extended_euclid(b, a % b)
    return d, t, s - (a // b) * t


def chinese_remainder(modulos):
    M = 1
    for m, a in modulos:
        M *= m

    x = 0
    for m, a in modulos:
        Mi = M // m
        x += extended_euclid(m, Mi)[2] * Mi * a

    return x + (-1 * (x // M) * M) if x < 0 else x


def print_robots(robots, seconds):
    print(f"After {seconds} seconds:")
    for r in range(width):
        for c in range(height):
            if any(robot.py == r and robot.px == c for robot in robots):
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print("")


def calculate_safety_factor(robots):
    quadrants = defaultdict(int)
    mx = floor(width / 2)
    my = floor(height / 2)
    for robot in robots:
        if robot.px < mx and robot.py < my:
            quadrants[0] += 1
        elif robot.px > mx and robot.py < my:
            quadrants[1] += 1
        elif robot.px < mx and robot.py > my:
            quadrants[2] += 1
        elif robot.px > mx and robot.py > my:
            quadrants[3] += 1

    return reduce(mul, quadrants.values())


def calculate_positions(robots, second):
    new_robots = []
    for robot in robots:
        px = (robot.px + second * robot.vx) % width
        py = (robot.py + second * robot.vy) % height
        new_robots.append(robot._replace(px=px, py=py))
    return new_robots


def check_pattern(robots, second):
    for r in range(height):
        same_row = sum(1 if robot.py == r else 0 for robot in robots)
        if same_row >= 20:
            return height, second
    for c in range(width):
        same_col = sum(1 if robot.px == c else 0 for robot in robots)
        if same_col >= 20:
            return width, second
    return None


def find_christmas_tree(robots):
    patterns = []
    # Iterate through first 100 seconds to find the 2 patterns
    for i in range(100):
        robots = calculate_positions(robots, 1)
        pattern = check_pattern(robots, i + 1)
        if pattern is not None:
            patterns.append(pattern)
            if len(patterns) == 2:
                break

    # Calculate seconds when christmas tree appears using CRT
    return chinese_remainder(patterns)


if __name__ == '__main__':
    robots = [Robot(*tuple(map(int, re.findall(r'(-?\d+)', line)))) for line in lines]

    safety_factor = calculate_safety_factor(calculate_positions(robots, 100))
    print(safety_factor)

    christmas_tree_seconds = find_christmas_tree(robots)
    print(christmas_tree_seconds)
