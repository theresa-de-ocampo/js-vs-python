# Sets - Exercise

# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

friends = {"John", "Michael", "Terry", "Eric", "Graham"}
my_friends = {"Reg", "Loretta", "Colin", "John", "Graham"}
cars = ["900", "420", "V70", "911", "996", "V90", "911", "911", "S", "328", "900"]

print(f"1. {'Eric' in friends and 'John' in friends}")

all_friends = friends.union(my_friends)
print(f"2. {all_friends}")

common_friends = friends.intersection(my_friends)
print(f"3. {common_friends}")

only_in_friends = friends.difference(my_friends)
print(f"4. {only_in_friends}")

unique_friends = friends.symmetric_difference(my_friends)
print(f"5. {unique_friends}")

deduplicated_cars = set(cars)
print(f"6. {deduplicated_cars}")
