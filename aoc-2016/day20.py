blacklist = []
for line in open("input/20.txt"):
    blacklist.append(tuple(map(int, line.strip().split("-"))))
blacklist = sorted(blacklist)

max_ip = 4294967295
allowed_regions = [[0, max_ip]]
for a, b in blacklist:
    for i, region in enumerate(allowed_regions.copy()):
        aa, ab = region
        if aa <= a <= ab < b:
            # New end
            allowed_regions[i][1] = a - 1
        elif a < aa <= b <= ab:
            # New start
            allowed_regions[i][0] = b + 1
        elif aa <= a <= b <= ab:
            # Entire blacklist rule inside region, split region in two
            allowed_regions.append([b + 1, allowed_regions[i][1]])
            allowed_regions[i][1] = a - 1
        elif a <= aa <= ab <= b:
            # Entire region blacklisted, remove it
            allowed_regions.pop(i)
            continue
        if allowed_regions[i][1] < allowed_regions[i][0]:
            allowed_regions.pop(i)

allowed_ip_count = 0
lowest_ip = max_ip
for a, b in allowed_regions:
    allowed_ip_count += b - a + 1
    lowest_ip = min(lowest_ip, a)

print(lowest_ip)
print(allowed_ip_count)
