class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(num):
            num = str(num)
            if len(num) % 2 :
                return False
            
            # 1234 => left_sum , right
            left_sum , right_sum = 0 , 0 
            i , j = 0 , len(num) - 1
            while(i < j):
                left_sum += int(num[i])
                right_sum += int(num[j])
                i += 1
                j -= 1
            return left_sum == right_sum
        res = 0
        for i in range(low,high + 1):
            if is_symmetric(i):
                res += 1

        return res        