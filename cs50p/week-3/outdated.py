# Could be optimized

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ")
        if date[0].isdigit():
            if is_middle_endian_num(date):
                convert_iso(date)
                break
        elif date[0].isalpha():
            if is_middle_endian_alpha(date):
                convert_iso(date)
                break

def is_middle_endian_num(date):
    try:
        month, day, year = date.strip().split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if month in range(1, 13):
            if day in range(1, 32):
                if len(str(year)) == 4:
                    return True
    except ValueError:
        return False

def is_middle_endian_alpha(date):
    try:
        month, day, year = date.split()
        day = int(day.replace(",", ""))
        year = int(year)
        if month in months:
            if day in range(1, 32):
                if len(str(year)) == 4:
                    return True
    except ValueError:
        return False

def convert_iso(date):
    if date[0].isdigit():
        month, day, year = date.split("/")
        print(f"{year}-{int(month):02}-{int(day):02}")
    elif date[0].isalpha():
        month, day, year = date.split()
        day = day.replace(",", "")
        month = months.index(month) + 1
        print(f"{year}-{month:02}-{int(day):02}")

main()
