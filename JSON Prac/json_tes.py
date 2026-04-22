import json
import os

def gather():
    data = {
        "first_name" : input("First Name : "),
        "last_name" : input("Last Name : ")
    }
    return data
    

def save_data(data):
    filename = "name_data.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            all_data = json.load(f)
    else:
        all_data = []

    all_data.append(data)

    with open(filename, "w") as j:
        json.dump(all_data, j, indent=4)


def show_data():
    filename = "name_data.json"

    if os.path.exists(filename):
        with open(filename, "r") as r:
            all_data = json.load(r)
    else:
        all_data = []

    for i, item in enumerate(all_data):
        print(f'{i + 1}. User Fisrt Name : {item["first name"]}, User Last Name : {item["last name"]}')


def delete_data():
    filename = "name_data.json"

    if os.path.exists(filename):
        with open(filename, "r") as r:
            all_data = json.load(r)
    else:
        all_data = []

    all_data.pop(0)

    with open(filename, "w") as j:
        json.dump(all_data, j, indent=4)


while True:
    
    v = gather()
    save_data(v)

    user_input = input("Do You Want to proceed? Y/N ").lower()

    if user_input == "y":
        continue
    elif user_input == "n":
        break
    else:
        print("Please input correctly")
        
    

print("Quitted from the system")

show_data()