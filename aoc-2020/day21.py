from collections import defaultdict

lines = [line.strip() for line in open("input/21.txt")]

all_ingredients = defaultdict(int)
allergens = defaultdict(list)
for line in lines:
    words = line.split()
    allergen_section = False
    ingredients = set()
    for word in words:
        if word.startswith("(contains"):
            allergen_section = True
            continue

        if not allergen_section:
            all_ingredients[word] += 1
            ingredients.add(word)
        else:
            allergen = word[:-1] if word[-1] in ")," else word
            allergens[allergen].append(ingredients)

allergen_all = dict()
for allergen, ingredient_sets in allergens.items():
    allergen_all[allergen] = set.intersection(*ingredient_sets)

result = 0
for ingredient, count in all_ingredients.items():
    contained = any(ingredient in ingredients for ingredients in allergen_all.values())
    if not contained:
        result += count
print(result)

allergen_map = dict()
while len(allergen_map) < len(allergen_all):
    allergen, chosen = next((k, v.pop()) for k, v in allergen_all.items() if len(v) == 1)
    assert chosen
    allergen_map[allergen] = chosen
    for k, v in allergen_all.items():
        if chosen in v:
            v.remove(chosen)

allergic_ingredients = sorted(allergen_map.items(), key=lambda item: item[0])
print(",".join(x[1] for x in allergic_ingredients))
