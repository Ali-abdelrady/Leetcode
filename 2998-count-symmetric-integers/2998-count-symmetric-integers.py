class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0 
        def is_symmetric(num):
            num = str(num)
            if len(num) % 2:
                return False
            
            n = len(num) // 2
            return sum(int(d) for d in num[:n]) == sum(int(d) for d in num[n:])

        for num in range(low , high + 1):
            if is_symmetric(num):
                res += 1

        return res        