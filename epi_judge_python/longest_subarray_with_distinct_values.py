from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    seen = {}
    max_length = start = 0
    
    for i, e in enumerate(A):
        if e in seen and start <= seen[e]:
            start = seen[e] + 1
        else:
            max_length = max(max_length, i - start + 1)
        seen[e] = i
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
