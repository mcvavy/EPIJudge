from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:

    primes = []
    is_prime = [False if x == 0 or x == 1 else True for x in range(n+1)]

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
