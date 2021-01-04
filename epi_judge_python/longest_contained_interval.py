from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    distinct_elemts = set(A)
    max_length = 0
    while distinct_elemts:
        val = distinct_elemts.pop()
        
        lower_bound = val - 1
        while lower_bound in distinct_elemts:
            distinct_elemts.remove(lower_bound)
            lower_bound -= 1
        
        upper_bound = val + 1
        while upper_bound in distinct_elemts:
            distinct_elemts.remove(upper_bound)
            upper_bound += 1
        
        max_length = max(max_length, upper_bound - lower_bound - 1)
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
