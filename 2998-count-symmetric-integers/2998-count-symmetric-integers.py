class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(num):
            num = str(num)
            if len(num) % 2 :
                return False
            
            # 1234 => left_sum , right
            # [1,2,3,4,5] => sum
            n = len(num) // 2 
            return sum(int(d) for d in num[:n]) == sum(int(d) for d in num[n:])
        res = 0
        for i in range(low,high + 1):
            if is_symmetric(i):
                res += 1

        return res        