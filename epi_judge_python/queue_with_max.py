from test_framework import generic_test
from test_framework.test_failure import TestFailure


from collections import deque

class QueueWithMax:
    def __init__(self):
        self._entries = deque()
        self._max_entries = deque()
        
    def enqueue(self, x: int) -> None:
        self._entries.append(x)
        
        while self._max_entries and self._max_entries[-1] < x:
            self._max_entries.pop()
        self._max_entries.append(x)

    def dequeue(self) -> int:
        if self._entries:
            result = self._entries.popleft()
            if result == self._max_entries[0]:
                self._max_entries.popleft()
            return result
        raise IndexError("Empty queue")

    def max(self) -> int:
        if self._max_entries:
            return self._max_entries[0]
        raise IndexError("Empty queue")


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
