import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def find_empty(grid):
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 0:
                    return (row, column)
        return None

    def isCellPossible(grid, row, column, val):
        # Check row
        for col in range(9):
            if grid[row][col] == val:
                return False
        # Check Column
        for rw in range(9):
            if grid[rw][column] == val:
                return False
        # Check cell
        row0 = (row//3)*3
        col0 = (column//3)*3

        for r in range(3):
            for c in range(3):
                if grid[r+row0][c+col0] == val:
                    return False
        return True
    
    def bt(grid):
        find = find_empty(grid)

        if not find:
            return True
        else:
            row, column = find

        for i in range(1, 10):
            if isCellPossible(grid, row, column, i):
                grid[row][column] = i

                if bt(grid):
                    return True
                grid[row][column] = 0
        return False

    return bt(partial_assignment)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
