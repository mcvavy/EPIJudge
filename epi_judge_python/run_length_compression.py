from test_framework import generic_test
from test_framework.test_failure import TestFailure

def decoding(s: str) -> str:
    count = 0; result = []
    
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            result.append(c * count)
            count = 0
    return ''.join(result)


def encoding(s: str) -> str:
    res = ""
    i = 0
    while i < len(s):
        count = 1
        j = i
        while j < len(s) - 1 and s[j] == s[j + 1]:
            count += 1
            j += 1
        res += str(count) + s[j]
        i = j + 1
    return res


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
