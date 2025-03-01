class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        i , j = 0 , 0
        while i < n-1:
            if nums[i] != 0:
                if nums[i] == nums[i+1]:
                    res[j] = nums[i] * 2 
                    nums[i+1] = 0
                else:
                    res[j] = nums[i]
                j += 1
            i += 1
        
        res[j] = nums[i] if nums[i] != 0 else 0
        return res
        