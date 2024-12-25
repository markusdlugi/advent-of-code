import re
from collections import defaultdict, namedtuple
from enum import Enum

Connection = namedtuple("Connection", "a op b output")


class BitType(Enum):
    IN = 0
    FIRST_SUM = 1
    SUM = 2
    CARRY = 3
    CARRY_AND = 4
    CARRY_OR = 5
    OUT = 6


def interpret_as_binary(digits: list):
    return int("".join(reversed(digits)), 2)


def execute_wires(wires: dict, connections: list):
    executed = []
    while len(executed) < len(connections):
        for i, c in enumerate(connections):
            if i in executed or c.a not in wires or c.b not in wires:
                continue

            if c.op == "AND":
                wires[c.output] = wires[c.a] & wires[c.b]
            elif c.op == "OR":
                wires[c.output] = wires[c.a] | wires[c.b]
            elif c.op == "XOR":
                wires[c.output] = wires[c.a] ^ wires[c.b]

            executed.append(i)

    number = ['0'] * 46
    for wire, val in wires.items():
        if wire.startswith("z"):
            number[int(wire[1:])] = str(val)

    return interpret_as_binary(number)


def determine_bit_types(connections: list):
    bit_type = defaultdict(set)
    for c in connections:
        # We classify the output bits by their function, depending on the inputs and the operator used
        if (c.a[0] == "x" and c.b[0] == "y") or (c.a[0] == "y" and c.b[0] == "x"):
            bit_type[BitType.IN].update([c.a, c.b])
            if c.op == "AND":
                if c.a[1:] == "00":
                    bit_type[BitType.FIRST_SUM] = c.output
                bit_type[BitType.SUM].add(c.output)
            elif c.op == "XOR":
                bit_type[BitType.CARRY].add(c.output)
        else:
            if c.op == "AND":
                bit_type[BitType.CARRY_AND].add(c.output)
            elif c.op == "OR":
                bit_type[BitType.CARRY_OR].add(c.output)
            elif c.op == "XOR":
                bit_type[BitType.OUT].add(c.output)
    return bit_type


def find_illegal_out_wires(bit_type: dict):
    result = set()

    # z## bits may only be used as outputs, any other type would be illegal (except for first and last one...)
    for type, bits in bit_type.items():
        if type == BitType.OUT:
            continue
        for bit in bits:
            if re.match(r"z[0-9]{2}", bit):
                if (type == BitType.CARRY_OR and bit == "z45") or (type == BitType.CARRY and bit == "z00"):
                    continue
                result.add(bit)

    # Likewise, no other bit should be an out type
    for bit in bit_type[BitType.OUT]:
        if not re.match(r"z[0-9]{2}", bit):
            result.add(bit)

    return result


def find_illegal_in_wires(connections: list, bit_type: dict):
    result = set()
    for c in connections:
        allowed_types = []
        # Only certain types of bits are allowed for certain operations
        # This helps to detect when carry and sum bits are swapped
        if c.op == "AND" or c.op == "XOR":
            allowed_types = [BitType.IN, BitType.FIRST_SUM, BitType.CARRY, BitType.CARRY_OR]
        elif c.op == "OR":
            allowed_types = [BitType.SUM, BitType.CARRY_AND]
        if not any(c.a in bit_type[allowed] for allowed in allowed_types):
            result.add(c.a)
        if not any(c.b in bit_type[allowed] for allowed in allowed_types):
            result.add(c.b)
    return result


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/24.txt")]

    wires = defaultdict(int)
    connections = []
    for line in lines:
        if ": " in line:
            wire, val = line.split(": ")
            wires[wire] = int(val)

        elif "->" in line:
            connection = re.findall(r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", line)[0]
            connections.append(Connection(*connection))

    # Part 1
    print(execute_wires(wires, connections))

    # Part 2
    # To solve part 2 programmatically, we use a set of "simple" rules
    # This makes assumptions about the structure of the adder, and also, certain swaps wouldn't be detectable this way
    # But most likely, this should still be sufficient to cover all official inputs
    bit_type = determine_bit_types(connections)
    swapped_wires = set()
    swapped_wires.update(find_illegal_out_wires(bit_type))
    swapped_wires.update(find_illegal_in_wires(connections, bit_type))

    print(','.join(sorted(swapped_wires)))
