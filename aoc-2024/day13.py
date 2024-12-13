import re
from collections import namedtuple

from sympy import Symbol, Matrix, solve_linear_system

Machine = namedtuple('Machine', ['ax', 'ay', 'bx', 'by', 'px', 'py'])


def solve(machine: Machine):
    a, b = Symbol('a'), Symbol('b')
    system = Matrix(((machine.ax, machine.bx, machine.px), (machine.ay, machine.by, machine.py)))
    res = solve_linear_system(system, a, b)
    for value in res.values():
        if not value.is_integer:
            return 0, 0
    else:
        return res[a], res[b]


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/13.txt")]

    machines = []
    for line in lines:
        if line.startswith("Button A"):
            ax, ay = tuple(map(int, re.findall(r'Button A: X\+(\d+), Y\+(\d+)', line)[0]))
        elif line.startswith("Button B"):
            bx, by = tuple(map(int, re.findall(r'Button B: X\+(\d+), Y\+(\d+)', line)[0]))
        elif line.startswith("Prize"):
            px, py = tuple(map(int, re.findall(r'Prize: X=(\d+), Y=(\d+)', line)[0]))
            machines.append(Machine(ax, ay, bx, by, px, py))

    # Part 1
    print(sum(3 * a + b for a, b in map(solve, machines)))

    # Part 2
    corrected_machines = []
    for machine in machines:
        corrected_machines.append(machine._replace(px=machine.px + 10000000000000, py=machine.py + 10000000000000))

    print(sum(3 * a + b for a, b in map(solve, corrected_machines)))
