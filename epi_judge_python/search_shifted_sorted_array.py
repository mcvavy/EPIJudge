from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    start = 0; end = len(A) - 1
    
    while start < end:
        mid = (start + end)//2
        if A[mid] > A[end]:
            start = mid + 1
        else:
            end = mid
    return start


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
