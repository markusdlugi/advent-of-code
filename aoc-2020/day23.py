from timeit import default_timer as timer

start = timer()
puzzle = int(open("input/23.txt").read())


def solve(p2):
    digits = str(puzzle)
    n = len(digits) if not p2 else 1_000_000
    cups = [0] * (n + 1)
    for i, x in enumerate(digits):
        next_ = int(digits[(i + 1) % len(digits)])
        cups[int(x)] = next_

    if p2:
        cups[int(x)] = len(digits) + 1
        for x in range(len(digits) + 1, n + 1):
            cups[x] = x + 1 if x < n else int(digits[0])

    max_number = max(cups)
    current_cup = int(digits[0])
    for i in range(10_000_000 if p2 else 100):
        picked_up = [cups[current_cup], cups[cups[current_cup]], cups[cups[cups[current_cup]]]]

        cups[current_cup] = cups[picked_up[-1]]

        destination = current_cup - 1
        while destination in picked_up or destination < 1:
            destination -= 1
            if destination < 1:
                destination = max_number

        cups[picked_up[-1]] = cups[destination]
        cups[destination] = picked_up[0]

        current_cup = cups[current_cup]

    if p2:
        one_after = cups[1]
        two_after = cups[cups[1]]
        return one_after * two_after
    else:
        curr = 1
        result = []
        while cups[curr] != 1:
            curr = cups[curr]
            result.append(curr)
        return "".join(str(x) for x in result)


print(solve(False))
print(solve(True))
end = timer()
print(f'Took {round((end - start) * 1000, 2)} ms.')
