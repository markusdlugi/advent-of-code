from itertools import product

lines = [line.strip() for line in open("input/14.txt")]

bitmask = None
mem_v1 = dict()
mem_v2 = dict()
for line in lines:
    if line.startswith("mask"):
        bitmask = line.split(" = ")[1]
    elif line.startswith("mem"):
        address, number = line.split(" = ")
        address = int(address[4:-1])
        number = int(number)
        value_bin = f"{number:036b}"
        address_bin = f"{address:036b}"

        floating = []
        assert bitmask is not None
        for i, v in enumerate(bitmask):
            # Change value in v1 if 0 or 1
            if v != "X":
                value_bin = value_bin[:i] + v + value_bin[i + 1:]

            # Change address in v2 if 1 or X
            if v == "1":
                address_bin = address_bin[:i] + v + address_bin[i + 1:]
            elif v == "X":
                floating.append(i)
        mem_v1[address] = int(value_bin, 2)

        for floating_bits in product(["0", "1"], repeat=len(floating)):
            address = address_bin
            for i, v in enumerate(floating_bits):
                bit = floating[i]
                address = address[:bit] + v + address[bit+1:]
            mem_v2[int(address, 2)] = number

print(sum(mem_v1.values()))
print(sum(mem_v2.values()))
