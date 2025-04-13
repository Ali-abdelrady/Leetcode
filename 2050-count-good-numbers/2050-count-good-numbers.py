class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD =  10**9 + 7
        divide = n // 2
        reminder = n % 2
        prime = pow(5,divide + reminder,MOD)
        even = pow(4,divide,MOD)
        return (prime * even) % MOD