from copy import deepcopy


def compute_checksum(disk: list):
    return sum(block_pos * int(file_id) if file_id != '.' else 0 for block_pos, file_id in enumerate(disk))


disk_map = open("input/09.txt").readline().strip()

block_pos = {}
file_size = {}
free_space = []
disk = []
for i, blocks in enumerate(disk_map):
    digit = int(blocks)
    if i % 2 == 0:
        file_id = i // 2
        file_size[file_id] = digit
        block_pos[file_id] = len(disk)
        disk.extend(digit * [file_id])
    else:
        free_space.append((len(disk), digit))
        disk.extend(digit * ['.'])

block_id_defrag = deepcopy(file_size)
counter = max(file_size.keys())
counter_old = 0
first = True
new_disk = deepcopy(disk)
for id, blocks in enumerate(new_disk):
    if block_pos[counter] < block_pos[counter_old]:
        if first:
            first = False
            new_disk[id - 1] = '.'
        new_disk[id] = '.'
        continue
    if blocks == '.':
        moved_block = block_id_defrag[counter]
        if moved_block <= 0:
            counter -= 1
            moved_block = block_id_defrag[counter]
        new_disk[id] = counter
        block_id_defrag[counter] = moved_block - 1
    else:
        old_block = block_id_defrag[counter_old]
        if old_block <= 0:
            counter_old += 1
            old_block = block_id_defrag[counter_old]
        block_id_defrag[counter_old] = old_block - 1

print(compute_checksum(new_disk))

counter = max(file_size.keys())
new_disk = deepcopy(disk)
for current in range(counter, -1, -1):
    old_id = block_pos[current]
    size = file_size[current]
    for index, (free_id, free_size) in enumerate(free_space):
        if free_id >= old_id:
            continue
        if free_size >= size:
            for i in range(size):
                new_disk[free_id + i] = current
                new_disk[old_id + i] = '.'
            if free_size - size == 0:
                del free_space[index]
            else:
                free_space[index] = (free_id + size, free_size - size)
            break

print(compute_checksum(new_disk))
