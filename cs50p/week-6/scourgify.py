import sys
import csv


def main():
    check_arg(sys.argv)
    before = sys.argv[1]
    after = sys.argv[2]
    write_new_csv(before, after)


def write_new_csv(before, after):
    try:
        if before.endswith(".csv"):
            with open(before) as csv_before:
                csv_reader = csv.DictReader(csv_before)
                fieldnames = ["first", "last", "house"]
                with open(after, "w") as csv_after:
                    csv_writer = csv.DictWriter(csv_after, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for row in csv_reader:
                        first, last = row["name"].removeprefix('"').removesuffix('""').split(",")
                        new_row = {
                            "first": first.strip(),
                            "last": last.strip(),
                            "house": row["house"]
                        }
                        csv_writer.writerow(new_row)
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")


def check_arg(arg):
    if len(arg) < 3:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
