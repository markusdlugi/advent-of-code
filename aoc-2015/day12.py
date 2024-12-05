import json


def sum_json(something, exclude_red):
    result = 0
    if isinstance(something, int):
        result += something
    elif isinstance(something, list):
        for item in something:
            result += sum_json(item, exclude_red)
    elif isinstance(something, dict):
        for value in something.values():
            if exclude_red and value == "red":
                return 0
            result += sum_json(value, exclude_red)
    return result


input_string = open("input/12.txt").read()
json_object = json.JSONDecoder().decode(input_string)

# Part A
print(sum_json(json_object, False))

# Part B
print(sum_json(json_object, True))
