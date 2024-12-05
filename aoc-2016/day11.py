from copy import deepcopy
import heapq
from itertools import combinations
from itertools import product
import time
import re


def is_final(floors):
    return sum(len(floors[x]["generators"]) + len(floors[x]["microchips"]) for x in range(3)) == 0


def is_possible(floors):
    for floor in floors:
        generator_count = len(floor["generators"])
        new_generator_count = len(floor["generators"].union(floor["microchips"]))
        if 0 < generator_count < new_generator_count:
            return False
    return True


def get_possible_moves(state, entry_count):
    floors = state[3]
    current_floor = next(i for i, x in enumerate(floors) if x["elevator"] == 1)
    available_items = set()
    available_items.update(("generators", x) for x in floors[current_floor]["generators"])
    available_items.update(("microchips", x) for x in floors[current_floor]["microchips"])
    possible_floors = [x for x in [current_floor - 1, current_floor + 1] if 0 <= x < len(floors)]
    # Only go down if there's something to get from there
    if current_floor - 1 in possible_floors and sum(
            len(floors[x]["generators"]) + len(floors[x]["microchips"]) for x in range(current_floor)) == 0:
        possible_floors.remove(current_floor - 1)
    result = []
    for item_count in [1, 2]:
        for items, next_floor in product(combinations(available_items, item_count), possible_floors):
            # If we have generator + microchip, ensure it's a pair, otherwise illegal
            if len(items) == 2:
                generators = sum([1 for x in items if x[0] == "generators"])
                microchips = sum([1 for x in items if x[0] == "microchips"])
                if generators == 1 and microchips == 1 and items[0][1] != items[1][1]:
                    continue
            # Build new state
            _, steps, _, floors, _ = deepcopy(state)
            steps += 1
            floors[current_floor]["elevator"] = 0
            floors[next_floor]["elevator"] = 1
            for item in items:
                floors[current_floor][item[0]].remove(item[1])
                floors[next_floor][item[0]].add(item[1])
            # Check if move is possible
            if not is_possible([floors[current_floor], floors[next_floor]]):
                continue
            # Possible move, append to result
            entry_count += 1
            result.append((get_cost(steps, floors), steps, entry_count, floors, build_floor_summary(floors)))
    return result


def build_floor_summary(floors):
    result = []
    for floor in floors:
        floor_summary = []
        for type in ["elevator", "generators", "microchips"]:
            floor_summary.append(len(floor[type]) if type != "elevator" else floor[type])
        result.append(tuple(floor_summary))
    return tuple(result)


def get_cost(steps, floors):
    # A* cost function
    # Cost from start is step count
    # Heuristic for cost to end is number of items in final floor (negative), weighted arbitrarily
    cost_from_start = steps
    cost_to_end = -(len(floors[3]["generators"]) + len(floors[3]["microchips"])) * 5
    return cost_from_start + cost_to_end


def find_smallest_steps(floors):
    # Cost, step count, entry count (pq discriminator), floors, floor summary (for visited set)
    start = (0, 0, 0, floors, build_floor_summary(floors))
    visited, priority_queue, entry_count = {start[4]}, [], 0
    heapq.heappush(priority_queue, start)
    while priority_queue:
        curr = heapq.heappop(priority_queue)
        _, step_count, _, curr_floors, _ = curr
        if is_final(curr_floors):
            return step_count
        possible_moves = get_possible_moves(curr, entry_count)
        for move in possible_moves:
            _, _, curr_entry_count, _, floor_summary = move
            if floor_summary not in visited:
                visited.add(floor_summary)
                heapq.heappush(priority_queue, move)
                entry_count = curr_entry_count


floors = []
for i in range(4):
    floors.append({"elevator": 1 if i == 0 else 0, "generators": set(), "microchips": set()})

for i, line in enumerate(open("input/11.txt")):
    floors[i]["generators"].update(re.findall(r'([a-z]+) generator', line))
    floors[i]["microchips"].update(re.findall(r'([a-z]+)-compatible', line))

# Part A
start_time = time.time()
print(find_smallest_steps(floors))
end_time = time.time()
#print("Took {} seconds.".format(str(end_time - start_time)))

# Part B
floors[0]["generators"].update(["elerium", "dilithium"])
floors[0]["microchips"].update(["elerium", "dilithium"])

start_time = time.time()
print(find_smallest_steps(floors))
end_time = time.time()
#print("Took {} seconds.".format(str(end_time - start_time)))
