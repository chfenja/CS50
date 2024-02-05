def main():
    text = input("Text: ")
    print(shorten(text))


def shorten(text):
    result = ""
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for c in text:
        if c not in vowels:
            result += c
    return f"{result}"


if __name__ == "__main__":
    main()
