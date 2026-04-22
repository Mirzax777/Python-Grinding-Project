class Parkinglot:
    def __init__(self, location):
        self.location = location
        self.spaces = []

    def car_in(self):
        name = input("Enter car owner name: ")
        car_brand = input("Enter car brand: ")
        plate = input("Enter license plate: ")
    
        car_data = {
            "name": name,
            "car": car_brand,
            "plate": plate
        }
        
        self.spaces.append(car_data)
        
        print(f"Car {car_brand} parked in {self.location}")


    def car_out(self):
        user_input = input("Please Insert License Plate : ")

        for i, car in enumerate(self.spaces):
            if car['plate'] == user_input:
                del self.spaces[i]
                found = True
                break
            
            if not found:
                print(f'Plate {user_input} not founf in {self.location}')



    def show_empty_space(self):
        total_space = 10
        occupy_space = len(self.spaces)
        empty_space = total_space - occupy_space
        print(f"{self.location}: {empty_space} empty, {occupy_space} occupied")


basement = Parkinglot('BASEMENT')
floor_1 = Parkinglot('1ST FLOOR')
floor_2 = Parkinglot('2ND FLOOR')


# Testing the Parking Lot System

print("=" * 50)
print("PARKING LOT SYSTEM TEST")
print("=" * 50)

# Test 1: Show empty spaces initially
print("\n--- Test 1: Initial Empty Spaces ---")
print(f"Basement: {basement.show_empty_space()}")
print(f"Floor 1: {floor_1.show_empty_space()}")
print(f"Floor 2: {floor_2.show_empty_space()}")

# Test 2: Add cars to basement
print("\n--- Test 2: Adding 3 Cars to Basement ---")
basement.car_in()  # User inputs: John, Toyota Avanza, B123
basement.car_in()  # User inputs: Sarah, Honda Civic, B456
basement.car_in()  # User inputs: Mike, Nissan Altima, B789

# Test 3: Check basement spaces after adding
print("\n--- Test 3: Basement Spaces After Adding ---")
print(f"Basement: {basement.show_empty_space()}")

# Test 4: Add cars to floor 1
print("\n--- Test 4: Adding 2 Cars to Floor 1 ---")
floor_1.car_in()  # User inputs: Alice, BMW X5, W111
floor_1.car_in()  # User inputs, David, Mercedes, W222

# Test 5: Check floor 1 spaces
print("\n--- Test 5: Floor 1 Spaces After Adding ---")
print(f"Floor 1: {floor_1.show_empty_space()}")

# Test 6: Remove a car from basement
print("\n--- Test 6: Removing Car from Basement ---")
basement.car_out()  # User inputs: B456 (Sarah's car)

# Test 7: Check basement after removal
print("\n--- Test 7: Basement After Removal ---")
print(f"Basement: {basement.show_empty_space()}")

# Test 8: Try removing a car that doesn't exist
print("\n--- Test 8: Try Removing Non-Existent Car ---")
basement.car_out()  # User inputs: Z999 (doesn't exist)

# Test 9: Add car to floor 2
print("\n--- Test 9: Adding 1 Car to Floor 2 ---")
floor_2.car_in()  # User inputs: Emma, Tesla Model 3, T333

# Test 10: Final summary
print("\n--- Test 10: Final Summary ---")
print(f"Basement: {basement.show_empty_space()}")
print(f"Floor 1: {floor_1.show_empty_space()}")
print(f"Floor 2: {floor_2.show_empty_space()}")

print("\n" + "=" * 50)
print("TEST COMPLETE")
print("=" * 50)