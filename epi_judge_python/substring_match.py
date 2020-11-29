from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    PRIME = 5381
    BASE = 257
    
    def get_hash(s: str) -> int:  
        s_hash = 0
        for i in range(len(s)):
            s_hash += (ord(s[i]) * (BASE**i))
        return s_hash%PRIME
        

    pattern_hash = get_hash(s)

    position = 0
    n = len(s) - 1
    for i in range(len(t)):
        curr_window = t[i: i + len(s)]
        if get_hash(curr_window) == pattern_hash:
            if s == curr_window:
                return i
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
