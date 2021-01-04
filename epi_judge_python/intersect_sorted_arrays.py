from typing import List

from test_framework import generic_test


from bisect import bisect_left

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    def isAlsoIn(other, item):
        item_index = bisect_left(other, item)
        return item_index < len(other) and other[item_index] == item
    
    return [x for i, x in enumerate(A) if (i == 0 or x != A[i-1]) and isAlsoIn(B, x)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
