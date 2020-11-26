from typing import List

from test_framework import generic_test


from typing import List

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if not square_matrix:
        return []
    
    res = []
    row_start = 0
    row_end = len(square_matrix) - 1
    
    col_start = 0
    col_end = len(square_matrix[0]) - 1
    
    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end + 1):
            res.append(square_matrix[row_start][col])
        
        for row in range(row_start + 1, row_end + 1):
            res.append(square_matrix[row][col_end])
        
        for col in reversed(range(col_start, col_end)):
            res.append(square_matrix[row_end][col])
        
        for row in reversed(range(row_start + 1, row_end)):
            res.append(square_matrix[row][col_start])
        
        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1
        
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
