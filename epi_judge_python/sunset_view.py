from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    res_stack = []
    
    for index, building in enumerate(sequence):
        while res_stack and building >= res_stack[-1][1]:
            res_stack.pop()
        res_stack.append((index, building))
    return [x[0] for x in reversed(res_stack)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
