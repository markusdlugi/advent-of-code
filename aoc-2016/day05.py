import hashlib

puzzle_input = 'cxdnnyjw'
hash_start = '00000'

pw1 = []
pw2 = [None] * 8
pw2_char_count = 0
for i in range(100_000_000):
    code = puzzle_input + str(i)
    digest = hashlib.md5(code.encode('utf-8')).hexdigest()
    if digest.startswith(hash_start):
        # Part A
        if len(pw1) < 8:
            pw1.append(digest[5])
            if len(pw1) == 8:
                print(*pw1, sep='')

        # Part B
        position = int(digest[5], 16)
        if position >= len(pw2) or pw2[position] is not None:
            continue
        pw2[position] = digest[6]
        pw2_char_count += 1
        if pw2_char_count == 8:
            break
print(*pw2, sep='')
