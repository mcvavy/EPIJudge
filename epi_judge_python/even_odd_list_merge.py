from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L
    
    even_pointer = even_list = ListNode()
    
    odd_pointer = odd_list = ListNode()
    
    pos = 0
    while L:
        if pos % 2 == 0:
            even_pointer.next = L
            even_pointer = even_pointer.next
        else:
            odd_pointer.next = L
            odd_pointer = odd_pointer.next
        L = L.next
        pos += 1
    
    odd_pointer.next = None
    even_pointer.next = odd_list.next
    return even_list.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
