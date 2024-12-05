import hashlib
import re


def find_keys(puzzle_input, stretched):
    result = []
    key_candidate = dict()
    three_pattern = r'\w*?(\w)\1\1\w*?'
    i = 0
    while len(result) < 64:
        # Generate digest
        code = puzzle_input + str(i)
        digest = hashlib.md5(code.encode('utf-8')).hexdigest()
        if stretched:
            for x in range(2016):
                digest = hashlib.md5(digest.encode('utf-8')).hexdigest()

        # Check for 5 of a kind for previous key candidates
        for k, v in key_candidate.copy().items():
            if i <= k + 1000:
                key, char = v
                if char * 5 in digest:
                    result.append(k)
                    key_candidate.pop(k)
            else:
                key_candidate.pop(k)

        # Check for 3 of a kind
        match = re.match(three_pattern, digest)
        if match is not None:
            key_candidate[i] = (digest, match.group(1))
        i += 1

    result = sorted(result)
    return result


puzzle_input = 'zpqevtbw'

# Part A
keys = find_keys(puzzle_input, False)
print(keys[63])

# Part B
keys = find_keys(puzzle_input, True)
print(keys[63])
