from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetry(leftSub: BinaryTreeNode, rightSub: BinaryTreeNode)-> bool:
        if not leftSub and not rightSub:
            return True
        elif leftSub and rightSub:
            return leftSub.data == rightSub.data and \
        check_symmetry(leftSub.left, rightSub.right) and \
        check_symmetry(leftSub.right, rightSub.left)
            
        return False
    return tree is None or check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
