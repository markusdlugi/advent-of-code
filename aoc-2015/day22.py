from collections import deque
from copy import deepcopy


def spell_bfs(player_stats, boss_stats, spells, hard_mode):
    queue = deque()
    min_mana = 5000
    winning = []
    state = dict()
    state["player"] = player_stats.copy()
    state["boss"] = boss_stats.copy()
    state["used"] = []
    state["used_mana"] = 0
    state["running"] = dict()
    state["nextspell"] = None
    queue.append(state)
    while len(queue) > 0:
        current = queue.popleft()
        if current["nextspell"] is not None:
            if current["used_mana"] >= min_mana:
                # No lower mana possible, abort
                continue
            result = simulate(current, hard_mode)
            if result == "winning":
                winning.append(current)
                min_mana = min(min_mana, current["used_mana"])
                continue
            elif result == "losing":
                continue
        possible = get_possible_spells(current, spells)
        for poss in possible:
            next_state = deepcopy(current)
            next_state["nextspell"] = poss
            queue.append(next_state)
    return winning


def get_possible_spells(state, spells):
    result = []
    for spell in spells:
        if spell[1] > state["player"]["mana"]:
            continue
        # > 1 because 'However, effects can be started on the same turn they end.'
        if spell[0] in state["running"] and state["running"][spell[0]][4] > 1:
            continue
        result.append(spell)
    return result


def simulate(state, hard_mode):
    # Player turn

    # Hard difficulty
    if hard_mode:
        state["player"]["hp"] -= 1
        if state["player"]["hp"] <= 0:
            return "losing"

    # Compute all multi turn spells
    for multispell in state["running"].values():
        if multispell[4] <= 0:
            continue
        multispell[4] -= 1
        state["boss"]["hp"] -= multispell[5]
        state["player"]["armor"] += multispell[6]
        state["player"]["mana"] += multispell[7]

    # Compute next spell effects
    spell = state["nextspell"]
    state["nextspell"] = None
    state["used"].append(spell)
    state["used_mana"] += spell[1]

    state["player"]["armor"] = 0
    state["player"]["mana"] -= spell[1]
    state["boss"]["hp"] -= spell[2]
    state["player"]["hp"] += spell[3]
    # New multi turn spell
    if spell[4] > 0:
        state["running"][spell[0]] = list(spell)

    if state["boss"]["hp"] <= 0:
        return "winning"

    # Boss turn
    # Compute all multi turn spells
    state["player"]["armor"] = 0
    for multispell in state["running"].values():
        if multispell[4] <= 0:
            continue
        multispell[4] -= 1
        state["boss"]["hp"] -= multispell[5]
        state["player"]["armor"] += multispell[6]
        state["player"]["mana"] += multispell[7]

    if state["boss"]["hp"] <= 0:
        return "winning"

    state["player"]["hp"] -= (state["boss"]["dmg"] - state["player"]["armor"])
    if state["player"]["hp"] <= 0:
        return "losing"


boss_stats = dict()
for line in open("input/22.txt"):
    stats = line.strip().split(": ")
    if stats[0] == "Hit Points":
        boss_stats["hp"] = int(stats[1])
    elif stats[0] == "Damage":
        boss_stats["dmg"] = int(stats[1])
    else:
        assert False

# Name, Mana, Dmg, Heal, Turns, Dmg/Turn, Armor/Turn, Mana/Turn
spells = [("Magic Missile", 53, 4, 0, 0, 0, 0, 0),
          ("Drain", 73, 2, 2, 0, 0, 0, 0),
          ("Shield", 113, 0, 0, 6, 0, 7, 0),
          ("Poison", 173, 0, 0, 6, 3, 0, 0),
          ("Recharge", 229, 0, 0, 5, 0, 0, 101)]

player_stats = dict()
player_stats["hp"] = 50
player_stats["mana"] = 500

# Part A
winning = spell_bfs(player_stats, boss_stats, spells, False)
winning = sorted(winning, key=lambda item: item["used_mana"])
print(winning[0]["used_mana"])
#print(list(map(lambda used: used[0], winning[0]["used"])))

# Part B
winning = spell_bfs(player_stats, boss_stats, spells, True)
winning = sorted(winning, key=lambda item: item["used_mana"])
print(winning[0]["used_mana"])
#print(list(map(lambda used: used[0], winning[0]["used"])))
