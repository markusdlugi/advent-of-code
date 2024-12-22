from collections import defaultdict

numbers = list(map(int, open("input/22.txt")))

secret_sum = 0
prices = defaultdict(list)
price_changes = defaultdict(list)
for i, num in enumerate(numbers):
    price = num % 10
    prices[i].append(price)

    for t in range(2000):
        prev = num
        prev_price = num % 10

        num ^= (num * 64)
        num %= 16777216

        num ^= (num // 32)
        num %= 16777216

        num ^= (num * 2048)
        num %= 16777216

        price = num % 10
        prices[i].append(price)

        price_change = price - prev_price
        price_changes[i].append(price_change)

    secret_sum += num

print(secret_sum)

buyer_count = len(numbers)

seq_sum = defaultdict(int)
for i in range(buyer_count):
    seen = set()
    for j in range(len(price_changes[i]) - 3):
        seq = tuple(price_changes[i][j:(j + 4)])
        if not seq in seen:
            seq_sum[seq] += prices[i][j + 4]
            seen.add(seq)

print(max(seq_sum.values()))
