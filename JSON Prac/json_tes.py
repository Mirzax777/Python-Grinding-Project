import json
import os

def load_data():
    filename = "name_data.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            all_data = json.load(f)
    else:
        all_data = []
    return all_data


def gather():
    all_data = load_data()
    pattern = "A"
    
    max_number = 0
    for item in all_data:
        id_data = item["id"]
        id_number = int(id_data[1:])      
        if id_number > max_number:
            max_number = id_number

    next_number = max_number + 1     
    custom_id =  f"{pattern}{next_number}"

    data = {
        "id" : custom_id,
        "first_name" : input("First Name : "),
        "last_name" : input("Last Name : ")
    }
    return data
    

def save_data(data):
    all_data = load_data()
    all_data.append(data)
    save_all_data(all_data)


def save_all_data(all_data):
    filename = "name_data.json"

    with open(filename, "w") as j:
        json.dump(all_data, j, indent=4)



def show_data():
    all_data = load_data()

    for i, item in enumerate(all_data):
        print(f'{i + 1}. User Fisrt Name : {item["first_name"]}, User Last Name : {item["last_name"]}')


def delete_data():
    all_data = load_data()
    n = int(input("Enter number to delete: "))
    all_data.pop(n-1)
    save_all_data(all_data)


def search_data():
    all_data = load_data()
    user_input = input("Input first name : ")

    found = False
    for item in all_data:
        if item["first_name"] == user_input:
            print(item)
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
        


def show_menu():
    print("\n" + "="*30)
    print("        DATA MANAGER")
    print("="*30)
    print("1. Add Data")
    print("2. Show Data")
    print("3. Delete Data")
    print("4. Search Data")
    print("5. Exit")
    print("="*30)


def menu():
    while True:
        show_menu()        
        user_input = input("Choose Option : ")

        if user_input == "1":
            data = gather()
            save_data(data)

        elif user_input == "2":
            show_data()

        elif user_input == "3":
            delete_data()

        elif user_input == "4":
            search_data()

        elif user_input == "5":
            print("You're Out")
            break

        else:
            print("Please Input Available Option.")


<<<<<<< HEAD
=======
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
        
>>>>>>> a1f922dcb93672dfed20c767ee6e394d28640525
    


