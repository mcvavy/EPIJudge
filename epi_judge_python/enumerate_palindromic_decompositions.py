from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    def generate(text, result, curr, start):
        if start == len(text):
            result.append(list(curr))
            return
        for i in range(start,len(text)):
            if text[start: i + 1] == text[start: i + 1][::-1]:
                generate(text, result, curr + [text[start: i + 1]], i + 1)
    
    result = []
    generate(text, result, [], 0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
