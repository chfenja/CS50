def convert(input):
    return input.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input("Enter your input: ")
    print(convert(user_input))

main()
