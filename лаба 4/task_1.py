import json


def task() -> float:
    filename = 'input.json'

    with open(filename) as f:
        data = json.load(f)
    sum_ = round(sum((item["score"] * item["weight"]) for item in data), 3)

    return sum_


print(task())
