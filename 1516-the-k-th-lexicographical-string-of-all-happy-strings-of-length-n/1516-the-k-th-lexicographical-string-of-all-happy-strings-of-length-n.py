class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        letters = ['a','b','c']
        def dfs(str):
            nonlocal k
            if len(str) == n :
                k -= 1
                res.append(str)
                return
            
            for ch in letters:
                if  k == 0 or (str != "" and ch == str[-1]):
                    continue
                dfs(str + ch)

        dfs("")
        return "" if k != 0 else res[-1]       