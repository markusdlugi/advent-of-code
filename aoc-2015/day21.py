import re
from collections import defaultdict
from itertools import combinations, product

boss = dict()
for line in open("input/21.txt"):
    stats = line.strip().split(": ")
    if stats[0] == "Hit Points":
        boss["hp"] = int(stats[1])
    elif stats[0] == "Damage":
        boss["dmg"] = int(stats[1])
    elif stats[0] == "Armor":
        boss["armor"] = int(stats[1])
    else:
        assert False

shop_pattern = r'(\w*[ ]?[+]?[\d]?)\s*(\d*)\s*(\d*)\s*(\d*)'
section = None
shop = defaultdict(list)
for line in open("input/21_shop.txt"):
    if line.startswith("Weapons"):
        section = "weapons"
    elif line.startswith("Armor"):
        section = "armor"
    elif line.startswith("Rings"):
        section = "rings"
    elif line.strip() != "":
        match = re.match(shop_pattern, line.strip())
        shop[section].append((match.group(1).strip(), int(match.group(2)), int(match.group(3)), int(match.group(4))))

player = dict()
winning = []
losing = []

for ring_count in range(3):
    for weapon, armor, rings in product(shop["weapons"], shop["armor"], combinations(shop["rings"], ring_count)):
        # Compute gold + stats
        gold = weapon[1] + armor[1]
        player["dmg"] = weapon[2]
        player["armor"] = armor[3]
        for ring in rings:
            gold += ring[1]
            player["dmg"] += ring[2]
            player["armor"] += ring[3]

        # Winning or losing
        if (player["dmg"] - boss["armor"]) >= (boss["dmg"] - player["armor"]):
            winning.append((gold, weapon[0], armor[0], list(map(lambda tup: tup[0], rings))))
        else:
            losing.append((gold, weapon[0], armor[0], list(map(lambda tup: tup[0], rings))))

winning = sorted(winning, key=lambda tup: tup[0])
losing = sorted(losing, key=lambda tup: tup[0], reverse=True)
print(winning[0][0])
print(losing[0][0])
