import re
from collections import namedtuple

from sympy import Symbol, Matrix, solve_linear_system

Machine = namedtuple('Machine', ['ax', 'ay', 'bx', 'by', 'px', 'py'])


def solve(machine: Machine):
    a, b = Symbol('a'), Symbol('b')
    system = Matrix(((machine.ax, machine.bx, machine.px), (machine.ay, machine.by, machine.py)))
    result = solve_linear_system(system, a, b)
    return (result[a], result[b]) if all(value.is_integer for value in result.values()) else (0, 0)


if __name__ == '__main__':
    all_lines = open("input/13.txt").read()

    machines = [Machine(*tuple(map(int, re.findall(r'(\d+)', group)))) for group in all_lines.split("\n\n")]

    # Part 1
    print(sum(3 * a + b for a, b in map(solve, machines)))

    # Part 2
    machines = list(map(lambda m: m._replace(px=m.px + 10000000000000, py=m.py + 10000000000000), machines))
    print(sum(3 * a + b for a, b in map(solve, machines)))
