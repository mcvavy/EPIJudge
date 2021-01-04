from typing import Iterator, List

from test_framework import generic_test

import heapq as q
def online_median(sequence: Iterator[int]) -> List[float]:
    maxQ = []; minQ = []
    res = []
    for item in sequence:
        if not maxQ or -maxQ[0] > item:
            q.heappush(maxQ, -item)
        else:
            q.heappush(minQ, item)
        if len(maxQ) > len(minQ) + 1:
            q.heappush(minQ, -maxQ[0])
            q.heappop(maxQ)
        elif len(minQ) > len(maxQ) + 1:
                q.heappush(maxQ, -minQ[0])
                q.heappop(minQ)
        if len(minQ) == len(maxQ):
            res.append(0.5 * (minQ[0] + -maxQ[0]))
        elif len(minQ) > len(maxQ):
            res.append(minQ[0])
        else:
            res.append(-maxQ[0])
    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
