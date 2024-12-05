from copy import deepcopy


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_multiplication(instructions, i, registers):
    result = 0
    if i < len(instructions) - 5:
        part = instructions[i:i + 5]
        if part[4][0] == "jnz" and part[4][1][1] == -5 and part[2][0] == "jnz" and part[2][1][1] == -2:
            a, b, res = part[4][1][0], part[2][1][0], part[0][1][0]
            registers[res] += registers[a] * registers[b]
            registers[a] = registers[b] = 0
            return 5
    if i < len(instructions) - 3:
        part = instructions[i:i + 3]
        if part[2][0] == "jnz" and part[2][1][1] == -2 and (part[0][0] == "inc" and part[1][0] == "dec") or (
                part[0][0] == "dec" and part[1][0] == "inc"):
            a, res = part[2][1][0], part[0][1][0] if part[0][0] == "inc" else part[1][1][0]
            registers[res] += registers[a]
            registers[a] = 0
            return 3
    return result


def run_program(instructions, registers):
    i = 0
    while i < len(instructions):
        cmd, args = instructions[i]

        if cmd == "cpy":
            x, y = args
            if is_int(y):
                i += 1
                continue
            registers[y] = x if is_int(x) else registers[x]
        elif cmd == "inc":
            mul = is_multiplication(instructions, i, registers)
            if not mul:
                registers[args[0]] += 1
            else:
                i += mul
                continue
        elif cmd == "dec":
            mul = is_multiplication(instructions, i, registers)
            if not mul:
                registers[args[0]] -= 1
            else:
                i += mul
                continue
        elif cmd == "jnz":
            x, y = args
            value = x if is_int(x) else registers[x]
            value2 = y if is_int(y) else registers[y]
            if value != 0:
                i += value2
                continue
        elif cmd == "tgl":
            value = args[0] if is_int(args[0]) else registers[args[0]]
            if i + value >= len(instructions) or 0 > i + value:
                i += 1
                continue
            ref_cmd, ref_args = instructions[i + value]
            if ref_cmd == "inc":
                ref_cmd = "dec"
            elif ref_cmd == "cpy":
                ref_cmd = "jnz"
            elif len(ref_args) == 1:
                ref_cmd = "inc"
            else:
                ref_cmd = "cpy"
            instructions[i + value] = (ref_cmd, ref_args)
        else:
            assert False

        i += 1


instructions = []
for line in open("input/23.txt"):
    line = line.strip()
    instruction = line.split(" ")
    args = instruction[1:]
    for i, arg in enumerate(args):
        args[i] = int(arg) if is_int(arg) else arg

    instructions.append((instruction[0], args))

# Part A
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
run_program(deepcopy(instructions), registers)
print(registers["a"])

# Part B
registers = {"a": 12, "b": 0, "c": 0, "d": 0}
run_program(deepcopy(instructions), registers)
print(registers["a"])
