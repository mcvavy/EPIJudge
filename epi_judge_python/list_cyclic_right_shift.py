from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L or k == 0:
        return L
    
    n = 1; tail = L
    while tail.next:
        n += 1
        tail = tail.next
    
    k %= n
    if k == 0:
        return L
    
    tail.next = L #Makes a cycle by connecting the tail to the head
    steps_to_new_head = n - k; new_tail = tail
    while steps_to_new_head:
        new_tail = new_tail.next
        steps_to_new_head -= 1
        
    new_head = new_tail.next
    new_tail.next = None
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
