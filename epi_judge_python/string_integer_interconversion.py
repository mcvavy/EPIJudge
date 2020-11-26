from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x < 10 and x > 0:
        return str(x)
    
    sign = '-' if x < 0 else ''
    x = abs(x)
    
    res = []
    while True:
        res.append(str(x % 10))
        x //= 10
        if x == 0:
            break

    return sign + ''.join(reversed(res))
    
    
def string_to_int(s: str) -> int:
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    
    if s[0] == '+':
        s = s[1:]
    
    n = len(s)
    
    res = 0
    for i in range(n):
        res = res * 10 + int(s[i])

    return res * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
