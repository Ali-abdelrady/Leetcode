class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        cnt = 0 
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == max_element:
                cnt += 1
            while cnt == k:
                res += len(nums) - right
                if nums[left] == max_element:
                    cnt -= 1
                left += 1    
        return res     