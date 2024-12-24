import re
from collections import defaultdict

lines = [line.strip() for line in open("input/24.txt")]


def interpret_as_binary(digits: list):
    return int("".join(reversed(digits)), 2)


def execute_wires(wires: dict, connections: list, swaps: list = None, exp_digits: list = None):
    if swaps is None:
        swaps = []

    # original_connection = connections.copy()

    executed = []
    wrong = set()
    while True:
        for i, (wire_a, op, wire_b, output) in enumerate(connections):
            if wire_a not in wires or wire_b not in wires:
                continue

            for swap in swaps:
                if output in swap:
                    idx = swap.index(output)
                    output = swap[(idx + 1) % 2]

            if op == "AND":
                wires[output] = wires[wire_a] & wires[wire_b]
            elif op == "OR":
                wires[output] = wires[wire_a] | wires[wire_b]
            elif op == "XOR":
                wires[output] = wires[wire_a] ^ wires[wire_b]
            else:
                raise ValueError("Panic!")

            if exp_digits is not None and output.startswith("z"):
                digit = int(output[1:])
                if exp_digits[digit] != wires[output]:
                    wrong.add(output)

            executed.append(i)

        if len(executed) == 0:
            break

        for ex in reversed(executed):
            del connections[ex]

        executed.clear()

    # while True:
    #     pre = len(wrong)
    #     new_wrong = set()
    #     for w in wrong:
    #         for (wire_a, op, wire_b, output) in original_connection:
    #             if output == w:
    #                 if not wire_a.startswith("x") and not wire_a.startswith("y"):
    #                     new_wrong.add(wire_a)
    #                 if not wire_b.startswith("x") and not wire_b.startswith("y"):
    #                     new_wrong.add(wire_b)
    #     wrong.update(new_wrong)
    #     if len(wrong) == pre:
    #         break
    # print(wrong)

    number = ['0'] * 100
    for wire, val in wires.items():
        if wire.startswith("z"):
            number[int(wire[1:])] = str(val)

    return interpret_as_binary(number)


wires = defaultdict(int)
connections = []
for line in lines:
    if ": " in line:
        wire, val = line.split(": ")
        val = int(val)
        wires[wire] = val

    elif "->" in line:
        wire_a, op, wire_b, output = re.findall(r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", line)[0]
        connections.append((wire_a, op, wire_b, output))

# # Replace Variable names to resemble the naming of a normal half-adder
# replacement = set()
# for wire_a, op, wire_b, output in connections:
#     if (wire_a.startswith("x") and wire_b.startswith("y")) or (wire_a.startswith("y") and wire_b.startswith("x")):
#         if op == "AND":
#             replacement.add((output, "s" + wire_a[1:]))
#         elif op == "XOR":
#             replacement.add((output, "c" + wire_a[1:]))
#
# for r_old, r_new in replacement:
#     for i, (wire_a, op, wire_b, output) in enumerate(connections):
#         if wire_a == r_old:
#             connections[i] = (r_new, op, wire_b, output)
#         elif wire_b == r_old:
#             connections[i] = (wire_a, op, r_new, output)
#         elif output == r_old:
#             connections[i] = (wire_a, op, wire_b, r_new)
#
# # Swap variables to always have same structure
# for i, (wire_a, op, wire_b, output) in enumerate(connections):
#     if wire_b.startswith("c"):
#         connections[i] = (wire_b, op, wire_a, output)
#     elif wire_b.startswith("x"):
#         connections[i] = (wire_b, op, wire_a, output)
#     elif wire_b.startswith("s"):
#         connections[i] = (wire_b, op, wire_a, output)
#
# # Print out sorted connections
# print(sorted(connections), sep="\n")

x, y = ["0"] * 100, ["0"] * 100
for wire, val in wires.items():
    if wire.startswith("x"):
        x[int(wire[1:])] = str(val)
    elif wire.startswith("y"):
        y[int(wire[1:])] = str(val)

x_num = interpret_as_binary(x)
y_num = interpret_as_binary(y)
print(f"x = {x_num}, y = {y_num}")

z_expected = x_num + y_num
print(f"Looking for {z_expected}")
print()

# Necessary swaps determined manually by examining list printed above
swaps = [('nqk', 'z07'), ('fpq', 'z24'), ('z32', 'srn'), ('fgt', 'pcp')]

swapped_wires = []
for x, y in swaps:
    swapped_wires.extend([x, y])
print(f"Swapped wires: {','.join(sorted(swapped_wires))}")

result = execute_wires(wires.copy(), connections.copy(), swaps)
print(f"z = {result}")
if result == z_expected:
    print(f"FOUND with swaps: {swaps} ({','.join(sorted(swapped_wires))})")
