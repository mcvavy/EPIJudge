from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)

    for i in range(n):
        for j in range(i, n):
            square_matrix[j][i], square_matrix[i][j] = square_matrix[i][j], square_matrix[j][i]
            
    for i in range(len(square_matrix)):
        
        start = 0
        end = len(square_matrix[i]) - 1
        
        while start < end:
            square_matrix[i][start],square_matrix[i][end] = square_matrix[i][end],square_matrix[i][start]
            
            start += 1
            end -= 1


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
