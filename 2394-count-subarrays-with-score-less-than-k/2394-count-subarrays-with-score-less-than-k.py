class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = 0 
        res = 0 
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum * (j - i + 1) >= k:
                sum -= nums[i]
                i += 1
            res += j - i + 1
        return res        