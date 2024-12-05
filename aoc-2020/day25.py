pubkeys = [int(line.strip()) for line in open("input/25.txt")]


def transform(base, pubkey):
    curr = 1
    for i in range(1, 20201227):
        curr *= base
        curr %= 20201227
        if curr == pubkey:
            return i
    else:
        return curr


loop_size = transform(7, pubkeys[0])
encryption_key = pow(pubkeys[1], loop_size, 20201227)
print(encryption_key)
