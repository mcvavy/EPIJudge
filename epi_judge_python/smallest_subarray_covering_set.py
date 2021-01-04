import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import Counter, namedtuple
Subarray = namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    res = Subarray(-1, -1)
    
    kwords = Counter(keywords)
    seen_words = Counter()
    left = 0
    for right,p in enumerate(paragraph):
        seen_words.update({p})
        if kwords - seen_words == Counter():
            while kwords - seen_words == Counter():
                if res == (-1, -1) or (right - left) < res[1] - res[0]:
                    res = (left, right)
                prev_left = left
                seen_words[paragraph[prev_left]] -= 1
                if seen_words[paragraph[prev_left]] == 0:
                    seen_words.pop(paragraph[prev_left])
                left += 1
    return res


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
