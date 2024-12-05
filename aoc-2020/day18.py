from collections import deque
import re


# Clean solution with overwritten int class
class StrangeInt(int):
    def __mul__(self, other):
        return StrangeInt(int(self) * int(other))

    def __truediv__(self, other):
        return StrangeInt(int(self) + int(other))

    def __pow__(self, other):
        return StrangeInt(int(self) + int(other))


lines = [line.strip() for line in open("input/18.txt")]

result1 = []
result2 = []
for line in lines:
    line = re.sub(r"(\d+)", r"StrangeInt(\1)", line)

    # Part A
    # Replace + with / to achieve same precedence as *
    line = line.replace("+", "/")
    result1.append(eval(line))

    # Part B
    # Replace + (now /) with ** to achieve higher precedence than *
    line = line.replace("/", "**")
    result2.append(eval(line))
print(sum(result1))
print(sum(result2))


# Old solution with stack fail
def eval_line_with_crazy_stack_logic(line, p2):
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    words = line.split()
    stack = deque()
    stackstack = deque()
    for word in words:
        if word in "+*":
            stack.append(word)
        elif word == "(":
            stackstack.append(stack.copy())
            stack.clear()
        elif word == ")":
            while len(stack) >= 3:
                if p2 and "+" in stack:
                    i = 0
                    while i + 2 < len(stack):
                        a = stack[i]
                        op = stack[i + 1]
                        b = stack[i + 2]
                        if op == "+":
                            result = eval(a + op + b)
                            del stack[i + 2]
                            del stack[i + 1]
                            stack[i] = str(result)
                            i += 3
                        else:
                            i += 2
                if len(stack) >= 3:
                    b = stack.pop()
                    op = stack.pop()
                    a = stack.pop()
                    result = eval(a + op + b)
                    stack.append(str(result))
            result = stack.pop()
            stack.clear()
            stack.extend(stackstack.pop())
            stack.append(str(result))
            if len(stack) >= 3 and (not p2 or stack[-2] == "+"):
                b = stack.pop()
                op = stack.pop()
                a = stack.pop()
                result = eval(a + op + b)
                stack.append(str(result))
        else:
            if len(stack) >= 2 and (not p2 or stack[-1] == "+"):
                op = stack.pop()
                a = stack.pop()
                result = eval(a + op + word)
                stack.append(str(result))
            else:
                stack.append(word)
    stack.reverse()
    while len(stack) > 1:
        if p2 and "+" in stack:
            i = 0
            while i + 2 < len(stack):
                a = stack[i]
                op = stack[i + 1]
                b = stack[i + 2]
                if op == "+":
                    result = eval(a + op + b)
                    del stack[i + 2]
                    del stack[i + 1]
                    stack[i] = str(result)
                    i += 3
                else:
                    i += 2
        else:
            a = stack.pop()
            op = stack.pop()
            b = stack.pop()
            result = eval(a + op + b)
            stack.append(str(result))
    result = stack.pop()
    return int(result)


#result1 = [eval_line_with_crazy_stack_logic(line, False) for line in lines]
#result2 = [eval_line_with_crazy_stack_logic(line, True) for line in lines]
#print(sum(result1))
#print(sum(result2))
