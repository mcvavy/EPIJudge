from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    min_price, max_profit = float("inf"), 0.0
    
    first_profits = [0] * len(prices)
    
    for i, price in enumerate(prices):
        min_price = min(price, min_price)
        profit_today = price - min_price
        max_profit = max(profit_today, max_profit)
        
        first_profits[i] = max_profit
    #print(first_profits)
        
    max_price = float("-inf")
    for j in reversed(range(1, len(prices))):
        max_price = max(max_price, prices[j])
        max_profit = max(max_profit, first_profits[j-1] + max_price - prices[j])
        
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
