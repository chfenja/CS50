grocery_list = {}

while True:
    try:
        item = input().strip().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        break

for item, num in sorted(grocery_list.items()):
    print(f"{num}- {item}")
