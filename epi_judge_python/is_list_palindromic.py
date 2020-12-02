from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    def reverse_linked_list(L):
        prev = None
        next_node = current = L
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    if not L:
        return True
    
    slow = fast = L
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    slow_it = reverse_linked_list(slow); fast_it = L
    while slow_it and fast_it:
        if slow_it.data != fast_it.data:
            return False
        slow_it = slow_it.next; fast_it = fast_it.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
