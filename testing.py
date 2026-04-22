import json
import os

def gather_data():
    data = {
        "sleep" : input("Sleep Time : "),
        "wake" : input("Wake Time : "),
        "sugar" : input("Sugar Intake : "),
        "exercise" : (input("Exercise : Y/N")).lower() == "y",
        "mood" : int(input("Mood Level : ")),
        "focus" : int(input("Focus Level : "))

    }
    return data

def save_to_json(data):
    filename = "data.json"

    # load existing data
    if os.path.exists(filename):
        with open(filename, "r") as f:
            all_data = json.load(f)
    else:
        all_data = []

    # add new entry
    all_data.append(data)

    # save back
    with open(filename, "w") as f:
        json.dump(all_data, f, indent=4)


def analyze_sleep_pattern(data):
    pass



v = gather_data()
save_to_json(v)