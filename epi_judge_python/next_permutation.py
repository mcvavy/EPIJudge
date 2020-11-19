from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    pivot = len(perm) - 2
    
    while pivot >= 0 and perm[pivot] >= perm[pivot + 1]:
        pivot -= 1
    
    #pivot will decrease below zero if all entries in perm are 
    # strictly decreasing
    if pivot < 0:
        return []
    
    for i in reversed(range(pivot + 1, len(perm))):
        if perm[i] > perm[pivot]:
            perm[pivot], perm[i] = perm[i], perm[pivot]
            break
    
    perm[pivot + 1:] = reversed(perm[pivot + 1:])
    
    return perm

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
