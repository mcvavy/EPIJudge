from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    res = [[1], [1, 1]]
    if n <= 0:
        return []
    if n == 1:
        return [res[0]]
    
    for i in range(2, n):
        temp = []
        temp.extend([1])
        for j in range(len(res[i - 1]) - 1):
            temp.extend([res[i-1][j] + res[i-1][j+1]])
        temp.extend([1])
        res.append(temp)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
