class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative  = 0
        n = len(nums)
        i = 0
        while i < n and nums[i] <= 0 :
            if nums[i] < 0 :
                negative += 1
            i += 1

        pos = n - i
        return max(pos,negative)      