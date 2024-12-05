import re
from math import ceil


def scramble(text, instructions, reverse):
    for line in (reversed(instructions) if reverse else instructions):
        line = line.strip()
        if line.startswith("swap letter"):
            a, b = tuple(re.findall(r'\s(\w)(?:\s|$)', line))
            text = text.replace(a, "#")
            text = text.replace(b, a)
            text = text.replace("#", b)
        elif line.startswith("swap position"):
            a, b = tuple(map(int, re.findall(r'\d+', line)))
            if a > b:
                a, b = b, a
            text = text[:a] + text[b] + text[a + 1:b] + text[a] + (text[b + 1:] if b + 1 < len(text) else "")
        elif line.startswith("rotate left") or line.startswith("rotate right"):
            params = re.findall(r'(left|right) (\d+)', line)[0]
            rot = int(params[1]) % len(text)
            if params[0] == ("left" if not reverse else "right"):
                text = text[rot:] + text[:rot]
            else:
                text = text[-rot:] + text[:-rot]
        elif line.startswith("rotate based"):
            letter = re.findall(r'(\w)$', line)[0]
            pos = text.find(letter)
            if not reverse:
                rot = (1 + pos + (1 if pos >= 4 else 0)) % len(text)
                text = text[-rot:] + text[:-rot]
            else:
                pos = 8 if pos == 0 else pos
                rot = (ceil(pos / 2) + (0 if pos % 2 == 1 else 5)) % len(text)
                text = text[rot:] + text[:rot]
        elif line.startswith("reverse"):
            a, b = tuple(map(int, re.findall(r'\d+', line)))
            sub = text[a:b + 1]
            sub = sub[::-1]
            text = text[:a] + sub + text[b + 1:]
        elif line.startswith("move"):
            a, b = tuple(map(int, re.findall(r'\d+', line)))
            if reverse:
                a, b = b, a
            letter = text[a]
            if a < b:
                text = text[:a] + text[a + 1:b + 1] + letter + text[b + 1:]
            else:
                text = text[:b] + letter + text[b:a] + text[a + 1:]
    return text


part1_input = "abcdefgh"
part2_input = "fbgdceah"

instructions = list(open("input/21.txt"))

print(scramble(part1_input, instructions, False))
print(scramble(part2_input, instructions, True))
