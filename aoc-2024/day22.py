from collections import defaultdict, deque


def evolve_secret(secret: int):
    secret ^= (secret * 64)
    secret %= 16777216

    secret ^= (secret // 32)
    secret %= 16777216

    secret ^= (secret * 2048)
    secret %= 16777216

    return secret


if __name__ == '__main__':
    secrets = list(map(int, open("input/22.txt")))

    secret_sum = 0
    seq_sum = defaultdict(int)
    for i, secret in enumerate(secrets):
        seen = set()
        seq_window = deque([])
        for t in range(2000):
            prev_price = secret % 10

            secret = evolve_secret(secret)

            price = secret % 10
            price_change = price - prev_price

            seq_window.append(price_change)
            if len(seq_window) > 4:
                seq_window.popleft()
                seq = tuple(seq_window)
                if not seq in seen:
                    seq_sum[seq] += price
                    seen.add(seq)

        secret_sum += secret

    print(secret_sum)
    print(max(seq_sum.values()))
