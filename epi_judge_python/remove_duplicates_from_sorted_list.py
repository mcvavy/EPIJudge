from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    prev = ListNode(0, L)
    forward = prev.next
    
    while forward:
        forward = forward.next
        prev = prev.next
        
        while forward and prev.data == forward.data:
            forward = forward.next
            prev.next = forward
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
