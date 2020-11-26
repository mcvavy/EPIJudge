from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    T = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M":1000}
    
    accumulator = T[s[-1]]
    
    for i in reversed(range(len(s) - 1)):
        accumulator += (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]])
    
    return accumulator


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
