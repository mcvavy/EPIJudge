from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    hm = {data: i for i, data in enumerate(inorder)}
    
    def build(preorder, inorder, start, end):
        if start > end:
            return None
        
        node = BinaryTreeNode(preorder[build.preIndex])
        build.preIndex += 1
        
        if start == end: return node
        
        index = hm.get(node.data)
        
        node.left = build(preorder, inorder, start, index - 1)
        node.right = build(preorder, inorder, index + 1, end)
        
        return node
    build.preIndex = 0
    return build(preorder, inorder, 0, len(inorder) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
