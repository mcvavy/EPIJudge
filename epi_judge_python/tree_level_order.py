from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    
    res = []
    queue = [tree]
    
    while queue:
        res.append([node.data for node in queue])
        
        queue = [child for curr in queue for child in [curr.left, curr.right] if child]
    
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
