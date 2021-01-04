from typing import List
import heapq as q

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    
    maxHeap = []
    maxHeap.append((-A[0], 0))
    
    result = []
    
    for _ in range(k):
        item_index = maxHeap[0][1]
        result.append(-q.heappop(maxHeap)[0])
        
        left_child_index = (2 * item_index) + 1
        if left_child_index < len(A):
            q.heappush(maxHeap, (-A[left_child_index], left_child_index))
        right_child_index = (2 * item_index) + 2
        if right_child_index < len(A):
            q.heappush(maxHeap, (-A[right_child_index], right_child_index))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
