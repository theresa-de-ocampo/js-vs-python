from prettytable import PrettyTable

stores = [
    {
        "name": "Freelancing Shop",
        "items": {
            "brian": 70,
            "black knight": 20,
            "biccus diccus": 100,
            "grim reaper": 500,
            "minstrel": -15,
        },
    },
    {
        "name": "Antique Shop",
        "items": {
            "french castle": 400,
            "wooden grail": 3,
            "scythe": 150,
            "catapult": 75,
            "german joke": 5,
        },
    },
    {"name": "Pet Shop", "items": {"blue parrot": 10, "white rabbit": 5, "newt": 2}},
]


cart = []
updated_stores = []
purse = 1000
total_cost = 0

for store in stores:
    print(f"\nWelcome to {store['name']}!")

    table = PrettyTable(["Item", "Price"])
    for item, price in store["items"].items():
        table.add_row([item.title(), price])
    print(table)

    item_to_buy = input("\nWhat would you like to buy? ").lower()

    if item_to_buy in store["items"]:
        cart.append(item_to_buy)

        price = store["items"][item_to_buy]
        total_cost += price
        purse -= price
        print(f"Gold Left: {purse}")

        del store["items"][item_to_buy]

    updated_stores.append(store)

print(f"Items Bought: {', '.join(cart)}")
