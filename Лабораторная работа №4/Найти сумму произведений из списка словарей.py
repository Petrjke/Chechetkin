# TODO решите задачу
import json

def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    sum_multip = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_multip, 3)

print(task())
