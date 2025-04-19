class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1):
            minReq = lower - nums[i]
            maxReq = upper - nums[i]
            low = bisect.bisect_left(nums,minReq,i+1)
            high = bisect.bisect_right(nums,maxReq,i+1)
            res += high - low

        return res