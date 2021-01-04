from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    def search_helper(A, target, start, end, result):
        if start > end: return result
        
        mid = (start + end)//2
        
        if A[mid] == target:
            result = mid
            return search_helper(A, target, start, mid - 1, result)
        elif target < A[mid]:
            return search_helper(A, target, start, mid - 1, result)
        else:
            return search_helper(A, target, mid + 1, end, result)
    return search_helper(A, k, 0, len(A) - 1, -1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
