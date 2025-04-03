class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 2):
            for j in range(i+1,n):
                if nums[i] < nums[j] :
                    continue
                for k in range(j+1,n):
                    if nums[k] < 0 :
                        continue
                    res = max(res , (nums[i]-nums[j]) * nums[k])

        return res        