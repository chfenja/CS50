import requests
import sys


if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins_to_buy = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response_dict = r.json()
except requests.RequestException:
    print("An error occurred")
else:
    value = float(response_dict["bpi"]["USD"]["rate_float"])
    total = bitcoins_to_buy * value
    print(f"Total price: ${total:,.4f}")
