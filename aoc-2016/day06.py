from collections import Counter

result1 = ""
result2 = ""
for column in zip(*[x.strip() for x in open("input/06.txt")]):
    counter = Counter(column).most_common()
    result1 += counter[0][0]
    result2 += counter[-1][0]
print(result1)
print(result2)
