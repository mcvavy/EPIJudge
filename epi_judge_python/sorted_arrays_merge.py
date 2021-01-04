from typing import List, Tuple

from test_framework import generic_test


import heapq as hq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    minHeap: List[Tuple[int, int]] = []
    
    #build iterators for each array in sorted arrays
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    
    #Put the first element of each iterator in min heap
    for i, it in enumerate(sorted_arrays_iters):
        first = next(it, None)
        if first is not None:
            hq.heappush(minHeap, (first, i))
    
    result = []
    while minHeap:
        smallest, i = hq.heappop(minHeap)
        smallest_array_iter = sorted_arrays_iters[i]
        result.append(smallest)
        next_item = next(smallest_array_iter, None)        
        if next_item is not None:
            hq.heappush(minHeap, (next_item, i))
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
