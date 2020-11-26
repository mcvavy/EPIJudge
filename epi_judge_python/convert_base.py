from test_framework import generic_test

import string
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(b1, num_as_string: str) -> int:
        result = 0
        num_as_string = num_as_string[::-1]   
        for i in range(len(num_as_string)):
            result += string.hexdigits.index(num_as_string[i].lower()) * b1**i
        return result    
    
    sign = ''
    if num_as_string[0] == '-' or num_as_string[0] == '+':
        if num_as_string[0] == '-':
            sign = '-'
        
        num_as_string = num_as_string[1:]
        
    integer_b1 = construct_from_base(b1, num_as_string)
    
    res = []
    while True:
        res.append(string.hexdigits[integer_b1 % b2].upper())
        integer_b1 //= b2
        if integer_b1 == 0:
            break
            
    return sign + ''.join(reversed(res))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
