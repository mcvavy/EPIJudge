from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    def is_valid_part(s):
        # "00", "000", "01", etc. are not valid , but "0" is valid.
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)
    
    result = []
    parts = [None] * 4
    
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(i + 1, min(i + 4, len(s))):
                parts[1] = s[i:j]
                if is_valid_part(parts[1]):
                    for k in range(j + 1, min(j + 4, len(s))):
                        parts[2] = s[j:k]
                        parts[3] = s[k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
#                         print(parts)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
