def execute_commands(registers):
    i = 0
    while 0 <= i < len(commands):
        cmd = commands[i]

        if cmd[0] == "hlf":
            registers[cmd[1]] //= 2
        elif cmd[0] == "tpl":
            registers[cmd[1]] *= 3
        elif cmd[0] == "inc":
            registers[cmd[1]] += 1
        elif cmd[0] == "jmp":
            i += int(cmd[1])
            continue
        elif cmd[0] == "jie":
            if registers[cmd[1]] % 2 == 0:
                i += cmd[2]
                continue
        elif cmd[0] == "jio":
            if registers[cmd[1]] == 1:
                i += cmd[2]
                continue

        i += 1
    return registers["b"]


commands = []
for line in open("input/23.txt"):
    line = line.strip()

    param2 = None
    if "," in line:
        splitting = line.split(", ")
        param2 = splitting[1]
        line = splitting[0]
    splitting = line.split(" ")
    line = splitting[0]
    param1 = splitting[1]
    commands.append((line, param1, int(param2) if param2 is not None else param2))

print(execute_commands({"a": 0, "b": 0}))
print(execute_commands({"a": 1, "b": 0}))
