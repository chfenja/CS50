import csv
import sys
from tabulate import tabulate

# regular.csv: https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv
# sicilian.csv: https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv


def main():
    check_arg(sys.argv)
    filename = sys.argv[1]
    formtatted(filename)


def formtatted(filename):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            print(tabulate(csv_reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arg(arg):
    if len(arg) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 2:
        sys.exit("Too many command-line arguments")
    elif not arg[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
