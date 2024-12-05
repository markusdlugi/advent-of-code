from collections import Counter

lines = list(open("input/01.txt"))

left = []
right = []
for line in lines:
    a, b = map(int, line.split())
    left.append(a)
    right.append(b)

left.sort()
right.sort()
distance = sum(abs(left[i] - right[i]) for i in range(len(lines)))
print(distance)

left_count = Counter(left)
right_count = Counter(right)
similarity_score = sum(val * key * right_count[key] for key, val in left_count.items())
print(similarity_score)
