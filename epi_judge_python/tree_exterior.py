import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    def getLeftBoundary(tree, result):
        if tree and (tree.left is not None and tree.right is not None):
            if tree.left:
                result.append(tree)
                getLeftBoundary(tree.left, result)
            else:
                if tree.right:
                    result.append(tree)
                    getLeftBoundary(tree.right, result)
    
    def getLeafNode(tree, result):
        if not tree:
            return None
        
        if not tree.left and not tree.right:
            result.append(tree)
        getLeafNode(tree.left, result)
        getLeafNode(tree.right, result)
        
    def getRightBoundary(tree, result):
        if tree and (tree.left is not None and tree.right is not None):
            if tree.right:
#                 result.append(tree)
                getRightBoundary(tree.right, result)
                result.append(tree)
            else:
                if tree.left:
#                     result.append(tree)
                    getRightBoundary(tree.left, result)
                    result.append(tree)
    
    result = []
    getLeftBoundary(tree, result); getLeafNode(tree, result); getRightBoundary(tree.right, result)
    return result


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
