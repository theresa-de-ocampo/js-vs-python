class Pizza:
    def __init__(self, size, crust_type, toppings=[]):
        self.size = size
        self.crust_type = crust_type
        self._toppings = list(toppings)

    @property
    def toppings(self):
        return self._toppings

    def add_topping(self, topping):
        self._toppings.append(topping)
        return self._toppings

    def remove_topping(self, topping):
        if topping in self._toppings:
            self._toppings.remove(topping)
        return self._toppings

    def summary(self):
        print(f"Size: {self.size}in")
        print(f"Crust: {self.crust_type}")
        print(
            f"Toppings: {self._toppings if len(self._toppings) >= 1 else 'No toppings yet!'}"
        )


print("=== Marinara Pizza ===")
marinara_pizza = Pizza(
    12, "Italian Style Crust", ["Tomato Sauce ", "Garlic", "Oregano"]
)
marinara_pizza.add_topping("Olive Oil")
marinara_pizza.remove_topping("Garlic")
marinara_pizza.summary()

print("\n=== Hawaiian Pizza ===")
hawaiian_pizza = Pizza(16, "Thin Crust")
hawaiian_pizza.summary()
