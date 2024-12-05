import re

pattern = r'([\w-]*)-(\d*)\[(\w*)\]'
input_file = open("input/04.txt").read()
rooms = list(map(lambda x: (x[0].replace("-", ""), int(x[1]), x[2]), re.findall(pattern, input_file)))

sector_id_sum = 0
north_pole_sector_id = 0
for room in rooms:
    name, sector_id, checksum = room
    letters = sorted(name, key=lambda c: (name.count(c), -ord(c)), reverse=True)
    seen = set()
    unique_letters = [x for x in letters if x not in seen and not seen.add(x)]
    if "".join(unique_letters[:5]) == checksum:
        sector_id_sum += sector_id
        decrypted = [chr(((ord(x) - ord('a') + room[1]) % 26) + ord('a')) for x in name]
        if "".join(decrypted) == "northpoleobjectstorage":
            north_pole_sector_id = sector_id
print(sector_id_sum)
print(north_pole_sector_id)
