from test_framework import generic_test


def evaluate(expression: str) -> int:
    DELIMETER = ','
    intermediate_result = []
    token_expression = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }
    
    for token in expression.split(DELIMETER):
        if token in token_expression:
            intermediate_result.append(token_expression[token](intermediate_result.pop(),
                                                               intermediate_result.pop()))
        else:
            intermediate_result.append(int(token))
    return intermediate_result[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
