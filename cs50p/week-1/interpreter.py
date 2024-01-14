def main():
    expression = input("Enter the arithmetic expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    match y:
        case "+":
            addition = x + z
            print(f"{addition:.1f}")
        case "-":
            substraction = x - z
            print(f"{substraction:.1f}")
        case "*":
            multiplication = x * z
            print(f"{multiplication:.1f}")
        case "/":
            division = x / z
            print(f"{division:.1f}")

main()
