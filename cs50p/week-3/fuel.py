while True:
    fraction = input("Fraction: ")
    numerator, denominator = fraction.split("/")
    try:
        numerator = int(numerator)
        denominator = int(denominator)
        if numerator < 0 or denominator < 0:
            continue
        if numerator > denominator:
            continue
        fuel_in_tank = round((numerator / denominator) * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if fuel_in_tank <= 1:
            print("E")
        elif fuel_in_tank >= 99:
            print("F")
        else:
            print(f"{fuel_in_tank}%")
        break
