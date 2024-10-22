import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_matecoin = Decimal("0.0")
    total_money = Decimal("0.0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            total_matecoin += bought
            total_money -= bought * price
        elif trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            total_matecoin -= sold
            total_money += sold * price

    result = {
        "earned_money": str(total_money),
        "matecoin_account": str(total_matecoin),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
