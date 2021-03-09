import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    """
    items:       1,  2,  3, ... n
    item value: v1, v2, v3, ... v_n
    
    +---+---+---+
    |w0 |w1 | w2|
    +---+---+---+
    | a | b | c |
    +---+---+---+
    | d | e | f |
    +---+---+---+
    """
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for row in range(1, n + 1):
        for col in range(capacity + 1):
            if row == 0 or col == 0:
                dp[row][col] == 0
            elif items[row - 1][0] > col:
                dp[row][col] = dp[row-1][col]
            else:
                dp[row][col] = max(dp[row-1][col], items[row - 1][1] + dp[row - 1][col - items[row-1][0]])
    return dp[n][capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
