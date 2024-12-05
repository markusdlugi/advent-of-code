grid = [line.strip() for line in open("input/03.txt")]

# print(*grid, sep="\n")

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
for dc, dr in slopes:
    r, c = (0, 0)
    trees = 0
    while (r + 1) < len(grid):
        c = (c + dc) % len(grid[0])
        r += dr
        if grid[r][c] == "#":
            trees += 1
    results.append(trees)

print(results[1])

product = 1
for result in results:
    product *= result
print(product)
