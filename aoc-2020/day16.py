from collections import defaultdict

with open("input/16.txt") as field:
    sections = [section.splitlines() for section in field.read().split("\n\n")]

rules, your, nearby = sections
your = your[1:]
nearby = nearby[1:]

# Parse rules
fields = defaultdict(list)
for rule in rules:
    key, val = rule.split(": ")
    parts = val.split(" or ")
    for p in parts:
        a, b = [int(x) for x in p.split("-")]
        fields[key].append((a, b))

# Find invalid tickets
invalid = []
inv_tickets = []
for pos, t in enumerate(nearby):
    vals = [int(x) for x in t.split(",")]

    for fi, v in enumerate(vals):
        ticket_valid = any(a <= v <= b for fv in fields.values() for a, b in fv)
        if not ticket_valid:
            invalid.append(v)
            inv_tickets.append(pos)

# Solution Part A
print(sum(invalid))

# Remove invalid tickets
for t in sorted(inv_tickets, reverse=True):
    del nearby[t]

# Find options and negative options for fields
options = defaultdict(set)
negative_options = defaultdict(set)
for pos, t in enumerate(nearby):
    vals = [int(x) for x in t.split(",")]

    for fi, v in enumerate(vals):
        for fk, fv in fields.items():
            field_valid = any(a <= v <= b for a, b in fv)
            if field_valid:
                options[fi].add(fk)
            else:
                negative_options[fi].add(fk)

# Remove negative options
for pos, fields in negative_options.items():
    for field in fields:
        if field in options[pos]:
            options[pos].remove(field)

# Build mapping from position to field
field_map = dict()
while len(field_map) < len(options):
    pos, chosen = next((pos, fields.pop()) for pos, fields in options.items() if len(fields) == 1)
    assert chosen
    field_map[pos] = chosen
    for pos, fields in options.items():
        if chosen in fields:
            fields.remove(chosen)

# Solution Part B
result = 1
your_fields = [int(x) for x in your[0].split(",")]
for i, field in field_map.items():
    if field.startswith("departure"):
        result *= your_fields[i]
print(result)
