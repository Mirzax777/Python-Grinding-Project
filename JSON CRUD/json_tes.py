import json
import os

FILENAME = "name_data.json"


def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_all_data(all_data):
    with open(FILENAME, "w") as j:
        json.dump(all_data, j, indent=4)


def gather():
    all_data = load_data()
    pattern = "A"
    
    max_number = 0
    for item in all_data:
        id_number = int(item["id"][1:])
        if id_number > max_number:
            max_number = id_number

    custom_id = f"{pattern}{max_number + 1}"

    data = {
        "id": custom_id,
        "first_name": input("First Name : "),
        "last_name": input("Last Name : ")
    }
    return data
    

def save_data(data):
    all_data = load_data()
    all_data.append(data)
    save_all_data(all_data)


def show_data():
    all_data = load_data()

    if not all_data:
        print("No data available.")
        return

    print("\n--- User List ---")
    for i, item in enumerate(all_data):
        print(f'{i + 1}. [{item["id"]}] {item["first_name"]} {item["last_name"]}')


def delete_data():
    all_data = load_data()

    if not all_data:
        print("No data available.")
        return

    show_data()

    user_input = input("Enter number to delete: ")

    try:
        n = int(user_input) - 1

        if n < 0 or n >= len(all_data):
            print("Invalid selection")
            return

    except ValueError:
        print("Please enter a valid number")
        return

    all_data.pop(n)
    save_all_data(all_data)
    print("Data deleted successfully.")


def search_data():
    all_data = load_data()
    user_input = input("Input first name : ").lower()

    found = False
    print("\n--- Search Result ---")

    for item in all_data:
        if user_input in item["first_name"].lower():
            print(f'[{item["id"]}] {item["first_name"]} {item["last_name"]}')
            found = True        

    if not found:
        print("Data Not Found")


def update_data():
    all_data = load_data()

    if not all_data:
        print("No data available.")
        return
    
    show_data()

    user_input = input("Choose Data You Want to Change : ")

    try:
        n = int(user_input) - 1

        if n < 0 or n >= len(all_data):
            print("Invalid selection")
            return 

    except ValueError:
        print("Please enter a valid number")
        return

    new_first = input("Enter Your New First Name (BLANK TO KEEP) : ")
    new_last = input("Enter Your New Last Name (BLANK TO KEEP) : ")

    item = all_data[n]

    if new_first != "":
        item["first_name"] = new_first

    if new_last != "":
        item["last_name"] = new_last

    save_all_data(all_data)
    print("Data updated successfully.")


def show_menu():
    print("\n" + "="*30)
    print("        DATA MANAGER")
    print("="*30)
    print("1. Add Data")
    print("2. Show Data")
    print("3. Delete Data")
    print("4. Search Data")
    print("5. Update Data")
    print("6. Exit")
    print("="*30)


def menu():
    while True:
        show_menu()        
        user_input = input("Choose Option : ")

        if user_input == "1":
            data = gather()
            save_data(data)
            print("Data added successfully.")

        elif user_input == "2":
            show_data()

        elif user_input == "3":
            delete_data()

        elif user_input == "4":
            search_data()

        elif user_input == "5":
            update_data()

        elif user_input == "6":
            print("You're Out")
            break

        else:
            print("Please Input Available Option.")

        input("\nPress Enter to continue...")


# Run program
menu()