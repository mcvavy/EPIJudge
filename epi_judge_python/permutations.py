from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    result = []
    if len(A) == 1:
        return [A[:]]
    
    for _ in enumerate(A):
        front = A.pop(0)
        perms = permutations(A)
        
        for perm in perms:
            perm.append(front)
        result.extend(perms)
        A.append(front)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
