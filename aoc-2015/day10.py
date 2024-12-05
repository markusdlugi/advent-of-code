def encode(string):
    result = ''
    prev = None
    count = 0
    for char in string:
        if prev is None or char == prev:
            count += 1
        else:
            result += str(count) + str(prev)
            count = 1
        prev = char
    result += str(count) + str(prev)
    return result


input_string = '3113322113'

# Part A
part_a = input_string
for i in range(40):
    part_a = encode(part_a)
print(len(part_a))

# Part B
part_b = input_string
for i in range(50):
    part_b = encode(part_b)
print(len(part_b))
