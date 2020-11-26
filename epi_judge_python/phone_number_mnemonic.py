from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    def phone_helper(result, chars):
        if not result:
            return list(chars)

    #     tempResult = []
    #     for word in words:
    #         for c in chars:
    #             tempResult.append(word + c)

    #     return tempResult

        return [word + c for word in result for c in chars]

    mappings = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")
    
    result = []
    
    for num in phone_number:
        result = phone_helper(result, mappings[int(num)])
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
