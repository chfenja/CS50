import sys


def main():
    check_arg(sys.argv)
    filename = sys.argv[1]
    line_count(filename)


def line_count(filename):
    count = 0
    try:
        with open(filename) as python_file:
            for line in python_file:
                if line.lstrip().startswith("#"):
                    continue
                elif line.strip() == "":
                    continue
                else:
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arg(arg):
    if len(arg) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 2:
        sys.exit("Too many command-line arguments")
    elif not arg[1].endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
