import sys
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes to find all primes up to `right`
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime

        primes = sieve(right)
        
        res = [-1, -1]
        min_diff = sys.maxsize
        prev_prime = -1

        for num in range(left, right + 1):
            if primes[num]:  # Check precomputed prime array
                if prev_prime != -1:
                    diff = num - prev_prime
                    if diff < min_diff:
                        min_diff = diff
                        res = [prev_prime, num]
                prev_prime = num
        
        return res
