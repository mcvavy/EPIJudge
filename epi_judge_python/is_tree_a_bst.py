from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def is_bst_helper(tree: BinaryTreeNode, low = float("-inf"), high = float("inf")) -> bool:
        if not tree:
            return True
        elif not low <= tree.data <= high:
            return False
        return is_bst_helper(tree.left, low, tree.data) and is_bst_helper(tree.right, tree.data, high)
    return is_bst_helper(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
