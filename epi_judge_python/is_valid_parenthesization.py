from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    pm = {
        ')': '(', ']':'[', '}': '{'
    }
    
    p_stack = []
    
    for c in s:
        if pm.get(c, None) not in p_stack:
            p_stack.append(c)
        else:
            if p_stack.pop() != pm.get(c, None):
                return False
    return len(p_stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
