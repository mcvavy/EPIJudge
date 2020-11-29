import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(L1: ListNode, L2: ListNode) -> ListNode:
    def list_length(L: ListNode):
        count = 0
        while L:
            L = L.next
            count += 1
        return count
    
    if not L1 or not L2:
        return None
    
    l1_length = list_length(L1); l2_length = list_length(L2)
    
    if l1_length < l2_length:
        L1, L2 = L2, L1
        
    # Advances the longer list to get equal length lists
    for _ in range(abs(l1_length - l2_length)):
        L1 = L1.next
    
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    
    return L1


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
