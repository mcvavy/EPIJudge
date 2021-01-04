from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def sumCal(tree: BinaryTreeNode, runningSum: int):
        if not tree: return 0
        runningSum = (runningSum << 1) + tree.data
        
        if not tree.left and not tree.right:
            return runningSum
        
        return sumCal(tree.left, runningSum) + sumCal(tree.right, runningSum)
    return sumCal(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
