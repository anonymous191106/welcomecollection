
# Smart Parking Allocation using CSP and Backtracking
#solts = [ {id:,type:,size:},{},{}]
size_value = {
    "small": 1,
    "medium": 2,
    "large": 3
}

types = ["normal", "ev", "disabled"]

# Check whether a slot can be assigned
def is_valid(vehicle, slot, assignment):

    if slot["id"] in assignment.values():
        return False

    if vehicle["type"] != slot["type"]:
        return False

    if size_value[vehicle["size"]] > size_value[slot["size"]]:
        return False

    return True


# Backtracking function
def backtrack(index, vehicles, slots, assignment):

    if index == len(vehicles):
        return True

    vehicle = vehicles[index]

    for slot in slots:
        if is_valid(vehicle, slot, assignment):

            assignment[vehicle["id"]] = slot["id"]

            if backtrack(index + 1, vehicles, slots, assignment):
                return True

            del assignment[vehicle["id"]]

    return False


# Display the result
def display_solution(assignment):

    print("\n===== SMART PARKING ALLOCATION =====")

    for vehicle, slot in assignment.items():
        print(vehicle, "->", slot)

    print("\nAll vehicles allocated successfully.")


# Take vehicle input
vehicles = []
n = int(input("Enter number of vehicles: "))

if n < 0:
    print("Invalid number of vehicles")
    raise SystemExit

print("\nEnter vehicle details: ID Type Size")
print("Type: normal / ev / disabled")
print("Size: small / medium / large")

for i in range(n):
    data = input(f"Vehicle {i + 1}: ").lower().split()

    if (len(data) != 3 or data[1] not in types
            or data[2] not in size_value):
        print("Invalid vehicle details")
        raise SystemExit

    vehicles.append({
        "id": data[0],
        "type": data[1],
        "size": data[2]
    })


# Take parking slot input
slots = []
m = int(input("\nEnter number of parking slots: "))

if m < 0:
    print("Invalid number of slots")
    raise SystemExit

print("\nEnter slot details: ID Type Size")

for i in range(m):
    data = input(f"Slot {i + 1}: ").lower().split()

    if (len(data) != 3 or data[1] not in types
            or data[2] not in size_value):
        print("Invalid slot details")
        raise SystemExit

    slots.append({
        "id": data[0],
        "type": data[1],
        "size": data[2]
    })


# Check for duplicate IDs
if (len(set(v["id"] for v in vehicles)) != n or
        len(set(s["id"] for s in slots)) != m):
    print("Duplicate IDs are not allowed")
    raise SystemExit


# Start allocation
assignment = {}

if backtrack(0, vehicles, slots, assignment):
    display_solution(assignment)
else:
    print("\nNo valid parking allocation found.")
