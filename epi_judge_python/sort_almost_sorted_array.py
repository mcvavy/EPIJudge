from typing import Iterator, List

from test_framework import generic_test

import itertools as t
import heapq as q

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    res = []
    minHeap = []
    for k in t.islice(sequence, k):
        q.heappush(minHeap, k)
    
    for k in sequence:
        item = q.heappushpop(minHeap, k)
        res.append(item)
    while minHeap:
        res.append(q.heappop(minHeap))
    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
