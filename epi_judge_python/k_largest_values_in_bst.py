from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def k_largest(tree):
        if tree and len(k_largest_elements) < k:
            k_largest(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                k_largest(tree.left)
        
    k_largest_elements = []
    k_largest(tree)
    return k_largest_elements


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
