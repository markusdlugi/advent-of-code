import re


def get_combo_operand(operand: int, a: int, b: int, c: int):
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    raise ValueError("Unexpected operand")


def execute_program(a: int, b: int, c: int, program: list):
    ip = 0
    output = []
    while 0 <= ip < len(program) - 1:
        jump = False
        instruction = program[ip]
        operand = program[ip + 1]
        if instruction == 0:
            a //= 2 ** get_combo_operand(operand, a, b, c)
        elif instruction == 1:
            b ^= operand
        elif instruction == 2:
            b = get_combo_operand(operand, a, b, c) % 8
        elif instruction == 3:
            if a != 0:
                jump = True
                ip = operand
        elif instruction == 4:
            b ^= c
        elif instruction == 5:
            output.append(get_combo_operand(operand, a, b, c) % 8)
        elif instruction == 6:
            b = a // 2 ** get_combo_operand(operand, a, b, c)
        elif instruction == 7:
            c = a // 2 ** get_combo_operand(operand, a, b, c)

        if not jump:
            ip += 2

    return output


def find_a(number: int, position: int, b: int, c: int, program: list):
    if position > len(program):
        return number

    number *= 8
    for i in range(0, 8):
        output = execute_program(number + i, b, c, program)
        if len(output) >= position and output[position * -1] == program[position * -1]:
            result = find_a(number + i, position + 1, b, c, program)
            if result:
                return result
    return None


if __name__ == '__main__':
    numbers = list(map(int, re.findall(r'(\d+)', open("input/17.txt").read())))

    a, b, c, program = numbers[0], numbers[1], numbers[2], numbers[3:]

    result = execute_program(a, b, c, program)
    print(*result, sep=",")

    result = find_a(0, 1, b, c, program)
    print(result)
