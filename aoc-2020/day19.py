from collections import defaultdict
import regex
from timeit import default_timer as timer

start = timer()
with open("input/19.txt") as field:
    sections = [section.splitlines() for section in field.read().split("\n\n")]

rules = sections[0]
messages = sections[1]


def parse_rules():
    rule_map = defaultdict(list)
    for rule in rules:
        n, r = rule.split(": ")
        n = int(n)
        if "\"" in r:
            rule_map[n].append(r[1])
        elif "|" in r:
            rule_map[n].extend(tuple(int(i) for i in x.split()) for x in r.split(" | "))
        else:
            rule_map[n].append(tuple(int(i) for i in r.split()))
    return rule_map


rule_map = parse_rules()


def build_regex(p2):
    result = "^"
    for i in rule_map[0][0]:
        part = build_regex_for_rule(i, p2)
        if isinstance(part, list):
            result += f"({'|'.join(part)})"
        else:
            result += part
    result += "$"
    return result


def build_regex_for_rule(n, p2):
    rule = rule_map[n]
    if "a" in rule or "b" in rule:
        return rule[0]

    # Special rules for part 2
    if p2:
        # Rule 8: Transform to (42)+
        if n == 8:
            option = build_regex_for_rule(rule[0][0], p2)
            return f"({'|'.join(option)})+"
        # Rule 11: Transform to recursive subpattern (42)(11)?(31)
        elif n == 11:
            parts = ["|".join(build_regex_for_rule(i, p2)) for i in rule[0]]
            return f"(?P<rule11>({parts[0]})(?&rule11)?({parts[1]}))"

    result = []
    for part in rule:
        option = ""
        for i in part:
            part_regex = build_regex_for_rule(i, p2)
            if isinstance(part_regex, list) and len(part_regex) > 1:
                option += f"({'|'.join(''.join(o) for o in part_regex)})"
            else:
                option += "".join(part_regex)
        result.append(option)
    return result


regex1 = build_regex(False)
print(sum(1 for m in messages if regex.match(regex1, m)))

regex2 = build_regex(True)
print(sum(1 for m in messages if regex.match(regex2, m)))

end = timer()
print(f'Took {end - start} seconds.')
