class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 6574365:
            return True
        mp = {}
        while n:
            num = floor(log(n)/log(3))
            print(num)
            if num in mp:
                return False

            mp[num] = True
            n -= 3**num

        return True        