from pandas import DataFrame
from wsimple.api import Wsimple

import config_loader
from one_time_password import get_one_time_password


def main():
    config = config_loader.get_config()

    ws = Wsimple(
        config["ws_login"],
        config["ws_password"],
        otp_callback=get_one_time_password,
    )

    if not ws.is_operational():
        raise RuntimeError("Wealthsimple is down!")

    holdings = {
        label: []
        for label in [
            "symbol",
            "name",
            "book_value",
            "book_currency",
            "market_value",
            "market_currency",
        ]
    }
    positions: dict = ws.get_positions()["results"]
    for result in positions:
        stock = result["stock"]
        holdings["symbol"].append(stock["symbol"])
        holdings["name"].append(stock["name"])
        book = result["book_value"]
        holdings["book_currency"].append(book["currency"])
        holdings["book_value"].append(book["amount"])
        market = result["market_book_value"]
        holdings["market_currency"].append(market["currency"])
        holdings["market_value"].append(market["amount"])

    holdings = DataFrame(holdings)

    holdings.to_csv("ws.csv", index=False)


if __name__ == "__main__":
    main()
