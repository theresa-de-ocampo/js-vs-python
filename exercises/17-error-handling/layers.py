def calculator():
    dividend = 30
    divisor = int(input("Enter a number <= 30: "))
    result = 30 / divisor


def invoice():
    try:
        calculator()
    except:
        raise


try:
    invoice()
except Exception as e:
    print(e)
