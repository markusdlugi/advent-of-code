from collections import deque
from functools import lru_cache


class Keypad:
    keypad = dict()

    def position(self, char: str):
        return self.keypad[char]

    def values(self):
        return self.keypad.values()


class NumericKeypad(Keypad):
    keypad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2),
    }

    def __hash__(self):
        return 0


class DirectionalKeypad(Keypad):
    keypad = {
        "^": (0, 1), 'A': (0, 2),
        "<": (1, 0), "v": (1, 1), ">": (1, 2)
    }

    def __hash__(self):
        return 1


def all_shortest_paths(start: tuple, end: tuple, allowed: set):
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    q = deque([(*start, [])])
    paths = set()
    min_len = None
    while q:
        r, c, path = q.popleft()

        if min_len is not None and len(path) > min_len:
            continue

        if (r, c) == end:
            if min_len is None:
                min_len = len(path)
            paths.add("".join(path) + "A")
            continue

        for direction, direction_value in directions.items():
            rr, cc = r + direction_value[0], c + direction_value[1]
            if not (rr, cc) in allowed:
                continue

            new_path = path.copy()
            new_path.append(direction)
            q.append((rr, cc, new_path))
    return paths


@lru_cache(3000)
def get_length_at_depth(sequence: str, depth: int, keypads: tuple):
    if depth == 0:
        return len(sequence)

    keypad = keypads[depth - 1]

    new_sequences = []
    current_pos = keypad.position('A')
    for char in sequence:
        next_pos = keypad.position(char)
        new_sequences.append(all_shortest_paths(current_pos, next_pos, keypad.values()))
        current_pos = next_pos

    result = 0
    for new_sequence in new_sequences:
        min_len = None
        for option in new_sequence:
            length = get_length_at_depth(option, depth - 1, keypads)
            if min_len is None or min_len > length:
                min_len = length
        result += min_len

    return result


def solve_keypad_conundrum(code: str, depth: int):
    keypads = (*[DirectionalKeypad()] * depth, NumericKeypad())
    length = get_length_at_depth(code, depth + 1, keypads)

    return length * int(code[:-1])


if __name__ == '__main__':
    codes = [line.strip() for line in open("input/21.txt")]

    complexity2 = sum(solve_keypad_conundrum(code, 2) for code in codes)
    print(complexity2)

    complexity25 = sum(solve_keypad_conundrum(code, 25) for code in codes)
    print(complexity25)
