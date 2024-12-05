import re

pattern = r'\s*(\d*)\s*(\d*)\s*(\d*)'
triangles = []
for line in open("input/03.txt"):
    triangles.append(tuple(map(int, re.findall(pattern, line.strip())[0])))

count = 0
for triangle in triangles:
    a, b, c = triangle
    if a + b > c and a + c > b and b + c > a:
        count += 1
print(count)

count = 0
for i in range(1, len(triangles), 3):
    for j in range(3):
        a, b, c = triangles[i-1][j], triangles[i][j], triangles[i+1][j]
        if a + b > c and a + c > b and b + c > a:
            count += 1
print(count)
