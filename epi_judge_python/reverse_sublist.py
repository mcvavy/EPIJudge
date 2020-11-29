from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if start == finish or not L:
        return L
    
    dummy_head = ListNode()
    dummy_head.next = L
    node_before_sublist = dummy_head
    
    count = 1
    while count < start:
        node_before_sublist = node_before_sublist.next
        count += 1
    
    pointer = node_before_sublist.next
    
    while start < finish:
        node_to_extract = pointer.next
        pointer.next = node_to_extract.next
        
        node_to_extract.next = node_before_sublist.next
        node_before_sublist.next = node_to_extract
        start += 1
        
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
