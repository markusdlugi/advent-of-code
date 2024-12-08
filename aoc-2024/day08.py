from collections import defaultdict


def find_antinodes(frequencies: dict, width: int, height: int, harmonics: bool):
    antinodes = set()
    for antennas in frequencies.values():
        if len(antennas) == 1:
            continue
        for r, c in antennas:
            for rr, cc in antennas:
                if r == rr and c == cc:
                    continue

                if harmonics:
                    antinodes.add((r, c))
                    antinodes.add((rr, cc))

                dr, dc = r - rr, c - cc

                ar1, ac1 = r + dr, c + dc
                while 0 <= ar1 < height and 0 <= ac1 < width:
                    antinodes.add((ar1, ac1))
                    if not harmonics:
                        break
                    ar1, ac1 = ar1 + dr, ac1 + dc

                ar2, ac2 = rr - dr, cc - dc
                while 0 <= ar2 < height and 0 <= ac2 < width:
                    antinodes.add((ar2, ac2))
                    if not harmonics:
                        break
                    ar2, ac2 = ar2 - dr, ac2 - dc
    return antinodes


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/08.txt")]

    width = len(lines[0])
    height = len(lines)
    frequencies = defaultdict(set)
    antennas = set()
    for r, line in enumerate(lines):
        for c, word in enumerate(line):
            if word != ".":
                frequencies[word].add((r, c))
                antennas.add((r, c))

    part1_antinodes = find_antinodes(frequencies, width, height, False)
    print(len(part1_antinodes))

    part2_antinodes = find_antinodes(frequencies, width, height, True)
    print(len(part2_antinodes))
