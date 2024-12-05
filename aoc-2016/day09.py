file = open("input/09.txt").read()


def get_decompressed_length(string, recursive):
    if "(" not in string or ")" not in string:
        return len(string)
    curr = 0
    length = 0
    while True:
        next_marker_start = string.find("(", curr)
        if next_marker_start == -1:
            break
        if next_marker_start > curr:
            length += len(string[curr:next_marker_start])
        next_marker_end = string.find(")", next_marker_start)
        size, rep = tuple(map(int, string[next_marker_start + 1:next_marker_end].split("x")))
        part = string[next_marker_end + 1:next_marker_end + 1 + size]
        part_length = get_decompressed_length(part, recursive) if recursive else len(part)
        length += part_length * rep
        curr = next_marker_end + 1 + size
    length += len(string[curr:])
    return length


print(get_decompressed_length(file, False))
print(get_decompressed_length(file, True))
