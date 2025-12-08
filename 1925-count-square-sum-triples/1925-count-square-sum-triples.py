class Solution:
    def countTriples(self, n: int) -> int:
        res = 0 
        if n < 3 :
            return 0

        for i in range(1,n-1):
            for j in range(i+1,n):
                distance = sqrt(i**2 + j**2)
                if distance.is_integer() and distance <= n:
                    res += 2 
        return res       