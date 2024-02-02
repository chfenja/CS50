from inflect import engine

names = []

while True:
    try:
        user_input = input().title()
        names.append(user_input)
    except EOFError:
        break

e = engine()
result = e.join(names)
result = "Adieu, adieu, to " + result
print(result)
