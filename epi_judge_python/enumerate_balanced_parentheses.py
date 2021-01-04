from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def generate(result, s, o, c, n):
        if len(s) == n * 2:
            result.append(s)
            return
        if o < n:
            generate(result, s + "(", o + 1, c, n)
        
        if c < o:
            generate(result, s + ")", o, c + 1, n)
            
    result = []
    generate(result, "", 0, 0, num_pairs)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
