class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        mp = Counter(nums)
        n = len(nums[0])
        def dfs(str):
            if len(str) == n:
                return str if str not in mp else None
            
            for ch in ['0','1']:
                res = dfs(str + ch)
                if res is not None:
                    return res
            
            return None

        return dfs("")
        