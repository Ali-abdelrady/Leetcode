class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i , j =  0 , 2
        res = 0
        while j < len(nums):
            subArr = nums[i:j+1]
            if subArr[0] + subArr[2] == subArr[1] / 2:
                res += 1
            i += 1
            j += 1
        return  res

