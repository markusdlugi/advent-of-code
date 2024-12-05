def run_program(instructions, registers):
    i = 0
    while i < len(instructions):
        cmd = instructions[i]

        if cmd.startswith("cpy"):
            _, x, y = cmd.split(" ")
            registers[y] = int(x) if x.isdigit() else registers[x]
        elif cmd.startswith("inc"):
            _, x = cmd.split(" ")
            registers[x] += 1
        elif cmd.startswith("dec"):
            _, x = cmd.split(" ")
            registers[x] -= 1
        elif cmd.startswith("jnz"):
            _, x, y = cmd.split(" ")
            value = int(x) if x.isdigit() else registers[x]
            if value != 0:
                i += int(y)
                continue
        else:
            assert False

        i += 1


instructions = []
for line in open("input/12.txt"):
    instructions.append(line.strip())

# Part A
registers = {"a": 0, "b": 0, "c": 0, "d": 0}
run_program(instructions, registers)
print(registers["a"])

# Part B
registers = {"a": 0, "b": 0, "c": 1, "d": 0}
run_program(instructions, registers)
print(registers["a"])
