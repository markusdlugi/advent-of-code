from collections import deque
from timeit import default_timer as timer

elf_count = 3012210

# Part A naive
def solve_old_a():
    start_time = timer()
    presents = []
    for i in range(elf_count):
        presents.append((i, 1))

    while len(presents) > 1:
        new_presents = []
        for i, elf in enumerate(presents):
            n, p = elf
            if p == 0:
                continue
            left_neighbor = i + 1 if i < len(presents) - 1 else 0
            presents[i] = (n, p + presents[left_neighbor][1])
            presents[left_neighbor] = (presents[left_neighbor][0], 0)
            if left_neighbor == 0:
                new_presents[0] = (new_presents[0][0], 0)
            new_presents.append(presents[i])
        presents = new_presents

    print(presents[0][0] + 1)
    end_time = timer()
    print("Took {} seconds.".format(end_time - start_time))
    print()


# Part A closed form
start_time = timer()
print(int(bin(elf_count)[3:] + "1", 2))
end_time = timer()
#print("Took {} milliseconds.".format((end_time - start_time) * 1000))
#print()


# Part B w/ 2 queues
def solve_old_b():
    start_time = timer()
    left = deque()
    right = deque()

    for i in range(1, elf_count + 1):
        if i < (elf_count // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        last = None
        if len(left) > len(right):
            last = left.pop()
        else:
            last = right.pop()

        right.appendleft(left.popleft())
        left.append(right.pop())
    print(left[0])
    end_time = timer()
    print("Took {} seconds.".format(end_time - start_time))
    print()

# Part B closed form
start_time = timer()
pow_3 = 1
while pow_3 * 3 < elf_count:
    pow_3 *= 3
print(elf_count - pow_3 + max(elf_count - 2 * pow_3, 0))
end_time = timer()
#print("Took {} milliseconds.".format((end_time - start_time) * 1000))
#print()
