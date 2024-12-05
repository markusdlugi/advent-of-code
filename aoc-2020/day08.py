from copy import deepcopy


def run_command(program, ip, acc):
    command, arg = program[ip]
    if command == "acc":
        acc += int(arg)
    elif command == "jmp":
        ip += int(arg) - 1
    elif command == "nop":
        pass
    ip += 1
    return ip, acc


def run_program(program, acc, print_on_loop):
    ip = 0
    visited = {0}
    while ip < len(program):
        ip, acc = run_command(program, ip, acc)

        if ip not in visited:
            visited.add(ip)
        else:
            if print_on_loop:
                print(acc)
            return False, ip, acc
    return True, ip, acc


program = [line.strip().split() for line in open("input/08.txt")]

# Part A
run_program(program, 0, True)

# Part B
i = 0
program_copy = None
while i < len(program):
    command, arg = program[i]
    if command in ("jmp", "nop"):
        program_copy = deepcopy(program)
        program_copy[i][0] = "nop" if command == "jmp" else "jmp"
    else:
        i += 1
        continue

    terminated, ip, acc = run_program(program_copy, 0, False)
    if terminated:
        print(acc)
        break
    i += 1
