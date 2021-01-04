from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max = max; self.count = count
            
    def __init__(self):
        self.entries = []; self.cachedMax = []
        
    def empty(self) -> bool:
        return len(self.entries) == 0

    def max(self) -> int:
        if self.empty():
            return -1
        else:
            return self.cachedMax[-1].max

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            popItem = self.entries.pop()
            current_max = self.cachedMax[-1].max
            
            if popItem == current_max:
                if self.cachedMax[-1].count == 1:
                    self.cachedMax.pop()
                else:
                    self.cachedMax[-1].count -= 1
            return popItem

    def push(self, x: int) -> None:
        self.entries.append(x)
        
        if len(self.cachedMax) == 0:
            self.cachedMax.append(self.MaxWithCount(x, 1))
        else:
            current_max = self.cachedMax[-1].max
            
            if current_max == x:
                self.cachedMax[-1].count += 1
            elif x > current_max:
                self.cachedMax.append(self.MaxWithCount(x, 1))


# class Stack:
#     def __init__(self):
#         self.res = []
#     def empty(self) -> bool:
#         return len(self.res) == 0

#     def max(self) -> int:
#         if self.empty():
#             return -1
#         else:
#             return max(self.res)

#     def pop(self) -> int:
#         if self.empty():
#             return -1
#         else:
#             return self.res.pop()

#     def push(self, x: int) -> None:
#         self.res.append(x)

# class Stack:
#     def __init__(self):
#         self.entries = []
#         self.cachedMax = []
        
#     def empty(self) -> bool:
#         return len(self.entries) == 0

#     def max(self) -> int:
#         if self.empty():
#             return -1
#         else:
#             return self.cachedMax[-1][0]

#     def pop(self) -> int:
#         if self.empty():
#             return -1
#         else:
#             val = self.entries.pop()
#             if val == self.cachedMax[-1][0]:
#                 if self.cachedMax[-1][1] == 1:
#                     self.cachedMax.pop()
#                 else:
#                     self.cachedMax[-1] = (val, self.cachedMax[-1][1] - 1)
#             return val

#     def push(self, x: int) -> None:
#         self.entries.append(x)
        
#         if len(self.cachedMax) == 0:
#             self.cachedMax.append((x, 1))
#         else:
#             if self.cachedMax[-1][0] == x:
#                 self.cachedMax[-1] = (x, self.cachedMax[-1][1] + 1)
            
#             if self.cachedMax[-1][0] < x:
#                 self.cachedMax.append((x, 1))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
