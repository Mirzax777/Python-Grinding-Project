import json
import os

FILENAME = "task_data.json"



# Used Frequently / Utility
def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_all_data(all_data):
    with open(FILENAME, "w") as g:
        json.dump(all_data, g, indent=4)


def generate_id():
    all_data = load_data()
    prefix = "T"
    max_num = 0
    for item in all_data:
        id_num = int(item["id"][1:])
        if max_num < id_num:
            max_num = id_num
    
    task_id = f"{prefix}{id_num + 1}"
    return task_id


# Core Feature
def add_task():
    task_id = generate_id()
    title = input("Enter Task Title : ")

    print("\nChoose Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    while True:
        choice = input("Input : ")
        priority_map = {
            "1": "low",
            "2": "medium",
            "3": "high"
        }

        if choice in priority_map:
            priority = priority_map[choice]
            break
        else:
            print("Invalid input")

    data = {
        "id": task_id,
        "title": title,
        "priority": priority,
        "is_done": False

    }
    all_data = load_data()
    all_data.append(data)
    save_all_data(all_data)
    
        
def show_tasks():
    all_data = load_data()

    if not all_data:
        print("No Data Available")
        return
    
    print("\n--- Task List ---")
    for i, item in enumerate(all_data):
        status = "✅" if item["is_done"] else "❌"
        print(f'{i + 1}. [{item["id"]}] {item["title"]} | {item["priority"].upper()} | {status}')


def delete_task():
    pass


def mark_task():
    pass


def toggle_task_status():
    pass



# Controller
def menu():
    pass