class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        cur = 0
        res = 0
        for r in range(n):
            while cur & nums[r]:
                cur ^= nums[l]
                l += 1
            res = max(res , r - l  + 1)
            cur ^= nums[r]
        return res 
        