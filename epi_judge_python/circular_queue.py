from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2
    def __init__(self, capacity: int) -> None:
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.queue_size = 0

    def enqueue(self, x: int) -> None:
        if self.is_empty:
            self.front = self.rear = 0
            self.queue[self.rear] = x
            self.queue_size += 1
        elif self.is_full:
            self.__resize()
            self.rear = (self.rear + 1)%len(self.queue)
            self.queue[self.rear] = x
            self.queue_size += 1
        else:
            self.rear = (self.rear + 1)%len(self.queue)
            self.queue[self.rear] = x
            self.queue_size += 1

    def dequeue(self) -> int:
        res = -1
        if self.is_empty:
            raise IndexError("empty queue")
        elif self.front == self.rear:
            res = self.queue[self.front]
            self.front = self.rear = -1
            self.queue_size -= 1
        else:
            res = self.queue[self.front]
            self.front = (self.front + 1)%len(self.queue)
            self.queue_size -= 1
        return res
            
    def size(self) -> int:
        return self.queue_size
    
    @property
    def is_full(self):
        return (self.rear + 1)%len(self.queue) == self.front
    
    @property
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def __resize(self):
        temp_queue = [None] * (self.queue_size * self.SCALE_FACTOR)
        j = self.front
        i = 0
        
        while True:
            temp_queue[i] = self.queue[j]
            i += 1
            j = (j + 1) % len(self.queue)
            
            if(j == self.front):
                break
        
        self.front = 0
        self.rear = len(self.queue) - 1
        self.queue = temp_queue


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
