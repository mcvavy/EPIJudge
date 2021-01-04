from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []; s = []
    
    while True:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            if len(s) == 0:
                break
            popped = s.pop()
            result.append(popped.data)
            tree = popped.right
            
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
