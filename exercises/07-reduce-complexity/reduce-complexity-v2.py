def num_days(month):
    days = {
        "jan": 31,
        "feb": 28,
        "mar": 31,
        "apr": 30,
        "may": 31,
        "jun": 30,
        "jul": 31,
        "aug": 31,
        "sep": 30,
        "oct": 31,
        "nov": 30,
        "dec": 31,
    }
    n = days.get(month)

    if n:
        print("number of days in", month, "is", n)
    else:
        print("invalid month!")


num_days(input("Month: ").lower())
