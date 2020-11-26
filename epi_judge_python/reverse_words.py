import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reverse_range(start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
    s.reverse()
    
    space = ' '
    start_index = 0
    while True:
        end_index = start_index
        while end_index < len(s) and s[end_index] != space:
            end_index += 1
        
        if end_index == len(s): break
            
        #reverse the word in the range of start_index and end_index
        reverse_range(start_index, end_index - 1)
        start_index = end_index + 1
        
    #reverse last word, because space search does not cover this range
    reverse_range(start_index, len(s) - 1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
