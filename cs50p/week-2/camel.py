# Terribly inefficient

def main():
    camel_cased = input("camelCase: ")
    snake_cased = convert_to_snake(camel_cased)
    print("snake_cased:", snake_cased)

def convert_to_snake(word):
    to_snake = []
    for c in word:
        if c.isupper():
            c = c.replace(c, f"_{c.lower()}")
            to_snake.append(c)
        else:
            to_snake.append(c)
    return "".join(to_snake)

main()
