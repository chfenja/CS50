text = input("Text: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for c in text:
    if c in vowels:
        c = c.replace(c, "")
    no_vowels = "".join(c)
    print(no_vowels, end="")
print()
