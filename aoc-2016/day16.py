import re
from timeit import default_timer as timer


def calculate_checksum(initial_state, disk_size):
    # Reverse and invert a to get b
    a = initial_state
    b = "".join(map(lambda x: "1" if x == "0" else "0", a[::-1]))

    # Create list of separators
    separators = []
    while len(separators) * len(a) + 1 <= disk_size:
        inv = list(map(lambda x: not x, reversed(separators)))
        separators.append(False)
        separators.extend(inv)

    # Calculate chunk size, i.e., how many disk bits influence a checksum bit
    checksum_length = disk_size
    count = 0
    while checksum_length % 2 == 0:
        checksum_length //= 2
        count += 1
    chunk_size = 2 ** count

    # Calculate checksum
    checksum = ""
    sep_index = 0
    part_block = ""
    while len(checksum) < checksum_length:
        # We count the number of ones in the chunk
        ones = 0

        # Still got some left from previous iteration?
        leftover = len(part_block)
        if leftover > 0:
            ones += part_block.count("1")
            part_block = ""

        # Count number of full a + s + b + s
        full_blocks, remaining = divmod(chunk_size - leftover, ((len(a) + 1) * 2))

        # Count ones in separators
        ones += separators[sep_index:sep_index + full_blocks * 2].count(True)
        sep_index = sep_index + full_blocks * 2

        # Number of ones of a + b = len(a) because a = not b
        ones += len(a) * full_blocks

        # If we have a partial block, handle that
        if remaining > 0:
            s1 = "1" if separators[sep_index] else "0"
            s2 = "1" if separators[sep_index + 1] else "0"
            part_block = a + s1 + b + s2
            sep_index += 2
            ones += part_block[:remaining].count("1")
            part_block = part_block[remaining:]

        # Checksum bit is 1 if number of ones is even
        checksum += "1" if ones % 2 == 0 else "0"

    return checksum


puzzle_input = '00111101111101000'
length_a = 272
length_b = 35651584

start_time = timer()
print(calculate_checksum(puzzle_input, length_a))
end_time = timer()
#print("Took {} seconds.".format(end_time - start_time))


start_time = timer()
print(calculate_checksum(puzzle_input, length_b))
end_time = timer()
#print("Took {} seconds.".format(end_time - start_time))


# Naive Solution
def solve_old():
    start_time = timer()
    current = puzzle_input
    length = length_b
    while len(current) < length:
        b = current[::-1]
        current += "0" + "".join(map(lambda x: "1" if x == "0" else "0", b))

    data = current[:length]
    checksum = None
    while checksum is None or len(checksum) % 2 == 0:
        pairs = re.findall(r'.{2}', data)
        checksum = "".join(map(lambda x: "1" if x[0] == x[1] else "0", pairs))
        data = checksum

    print(checksum)
    end_time = timer()
    print("Took {} seconds.".format(end_time - start_time))
