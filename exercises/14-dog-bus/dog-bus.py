# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.
#    - Use MAX_SEATS to limit capacity.
#    - Dynamically assign the next seat number.
#    - Print the updated roster showing all pets after pickup.
#
# 4. Ask which pet leaves early.
#    - Remove that pet from the bus.
#    - Print a message saying they’ve headed home.
#
# 5. Print a final roster listing the remaining pets and their dropoff times.

import json

MAX_SEATS = 5

dogs = {
    1: {
        "name": "Athena",
        "breed": "Mini Pinscher",
        "pickup_time": "8:00 AM",
        "dropoff_time": "5:00 PM",
    },
    2: {
        "name": "Junior",
        "breed": "Shih Tzu",
        "pickup_time": "10:00 AM",
        "dropoff_time": "6:00 PM",
    },
}


def add_dog():
    add = input("Add a dog (Y/N): ").upper()

    if add == "Y":
        name = input("Name: ").title()
        breed = input("Breed: ").title()
        pickup_time = input("Pick-Up Time: ")
        dropoff_time = input("Drop Off Time: ")

        dogs[len(dogs) + 1] = {
            "name": name,
            "breed": breed,
            "pickup_time": pickup_time,
            "dropoff_time": dropoff_time,
        }

        print(json.dumps(dogs, indent=2))


print(json.dumps(dogs, indent=2))

if len(dogs) < MAX_SEATS:
    add_dog()

pet_to_remove = input("Which pet leaves early? ").title()

found = next(
    ((id, dog) for id, dog in dogs.items() if dog["name"] == pet_to_remove), None
)

if found:
    del dogs[found[0]]
    print(f"{found[1]["name"]} has headed home.")

print(json.dumps(dogs, indent=2))
