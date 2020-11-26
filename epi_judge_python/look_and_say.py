from test_framework import generic_test


def look_and_say(n: int) -> str:
    def next_number(s):
        result = []
        i = 0

        while i < len(s):
            count = 1
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1

        return ''.join(result)

    s = '1'
    for i in range(1, n):
#         print(s)
        s = next_number(s)
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
