from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

from bisect import bisect_right

def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    if not preorder_sequence:
        return None
    
    preIndex = [0]
    def buildTree(preorder, key, low, high, size):
        if preIndex[0] >= size or not preorder:
            return None
        
        node = None
        if low <= key <= high:
            node = BstNode(key)
            preIndex[0] += 1
            
            if preIndex[0] < size:
                node.left = buildTree(preorder, preorder[preIndex[0]], low, key - 1, size)
            if preIndex[0] < size:
                node.right = buildTree(preorder, preorder[preIndex[0]], key + 1, high, size)
        return node
    return buildTree(preorder_sequence, preorder_sequence[0], float("-inf"), float("inf"), len(preorder_sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
