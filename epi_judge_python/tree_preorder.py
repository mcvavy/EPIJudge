from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree: return []
    
    s = [tree]; result = []
    
    while s:
        current = s.pop()
        result.append(current.data)
        if current.right:
            s.append(current.right)
        if current.left:
            s.append(current.left)
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
