COKE_PRICE = 50
amount_due = COKE_PRICE
accepted_coins = [25, 10, 5]
total_inserted_coins = 0

while True:
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in accepted_coins:
        total_inserted_coins = inserted_coin + total_inserted_coins
        if total_inserted_coins < COKE_PRICE:
            amount_due = COKE_PRICE - total_inserted_coins
            print("Amount Due: ", amount_due)
            continue
        elif total_inserted_coins >= COKE_PRICE:
            change_owed = total_inserted_coins - COKE_PRICE
            print("Change Owed:", change_owed)
            break
    else:
        print("Amount Due:", amount_due)
