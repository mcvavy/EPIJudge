from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price, max_profit = float("inf"), 0.0
    
    for price in prices:
        min_price = min(price, min_price)
        profit_today = price - min_price
        max_profit = max(profit_today, max_profit)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
