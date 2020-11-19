from typing import List

from test_framework import generic_test


def multiply(A: List[int], B: List[int]) -> List[int]:
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    
    print("sign", sign)
    
    A[0],B[0] = abs(A[0]), abs(B[0])
    res = [0] * (len(A) + len(B))
    
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            res[i + j + 1] += A[i] * B[j]
            res[i+j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10
    
    res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]
    
    return [res[0] * sign ] + res[1:]
    
    res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]
    
    return [res[0] * sign ] + res[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
