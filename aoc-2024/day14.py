import re
from collections import namedtuple, defaultdict
from functools import reduce
from math import floor
from operator import mul

lines = [line.strip() for line in open("input/14.txt")]

Robot = namedtuple('Robot', ['px', 'py', 'vx', 'vy'])
width = 101
height = 103


def print_robots(robots, seconds):
    print(f"After {seconds} seconds:")
    for r in range(width):
        for c in range(height):
            if any(robot.px == r and robot.py == c for robot in robots):
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


def simulate_robots(robots, search_for_tree=True):
    safety_factor = 0
    for i in range(8200):
        new_robots = []
        for robot in robots:
            px = (robot.px + robot.vx) % width if robot.px + robot.vx >= 0 else width + robot.px + robot.vx
            py = (robot.py + robot.vy) % height if robot.py + robot.vy >= 0 else height + robot.py + robot.vy
            new_robots.append(robot._replace(px=px, py=py))
        robots = new_robots
        if i == 99:
            safety_factor = calculate_safety_factor(robots)
            if not search_for_tree:
                break
        if i > 100 and (i - 114) % 103 == 0:
            print_robots(robots, i + 1)

    return safety_factor


if __name__ == '__main__':
    robots = [Robot(*tuple(map(int, re.findall(r'(-?\d+)', line)))) for line in lines]

    safety_factor = simulate_robots(robots, False)
    print(safety_factor)
