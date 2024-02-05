def main():
    while True:
        try:
            fraction = get_input("Fraction: ")
            fuel_in_tank_perc = convert(fraction)
            print(gauge(fuel_in_tank_perc))
            break
        except (ValueError, ZeroDivisionError):
            pass


def get_input(prompt):
    return input(prompt)


def convert(fraction):
    numerator, denominator = fraction.split("/")
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        raise ValueError
    if denominator == 0:
        raise ZeroDivisionError
    if numerator < 0 or denominator < 0:
        raise ValueError
    if numerator > denominator:
        raise ValueError
    fuel_in_tank_perc = round((numerator / denominator) * 100)
    return fuel_in_tank_perc


def gauge(fuel_in_tank_perc):
    if fuel_in_tank_perc <= 1:
        return "E"
    elif fuel_in_tank_perc >= 99:
        return "F"
    else:
        return f"{fuel_in_tank_perc}%"


if __name__ == "__main__":
    main()
