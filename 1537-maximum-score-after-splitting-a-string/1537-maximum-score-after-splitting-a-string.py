class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count('1')
        zero = 0 
        max_sum = 0
        for ch in s[:-1] :
            if ch == '0':
                zero += 1
            else:
                one -= 1
            max_sum = max(max_sum,zero + one)

        return max_sum            