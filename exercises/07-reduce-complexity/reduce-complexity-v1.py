def num_days(month):
    months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]

    if month == "" or month not in months:
        print("Invalid month!")
    else:
        i = months.index(month)

        if i == 1:
            print("number of days in", month, "is", 28)
        elif i % 2 == 0:
            print("number of days in", month, "is", 31)
        else:
            print("number of days in", month, "is", 30)


num_days(input("Month: ").lower())
