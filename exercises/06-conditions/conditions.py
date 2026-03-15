print("if elif else - Exercise")
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

n1 = float(input("First Number: "))
operator = input("Operator: ")
n2 = float(input("Second Number: "))
celsius_str = input("Celsius: ")

print(" ")
if operator == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif operator == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif operator == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif operator == "/":
    print(f"{n1} / {n2} = {n1 / n2}")
else:
    print("Unknown Operator")

if celsius_str != "":
    celsius = float(celsius_str)
    print(f"{round(celsius, 2):.2f}°C is {round(celsius*9/5+32, 2):.2f}°F")
