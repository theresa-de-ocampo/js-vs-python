try:
    dividend = 30
    divisor = int(input("Enter a number <= 30: "))

    if divisor > 30:
        raise ValueError("Number must be <= 30")

    result = 30 / divisor

except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("An unexpected error occurred")
else:
    print(f"{dividend} / {divisor} = {round(result, 2):.2f}")
print("** Thank you for playing! **")
