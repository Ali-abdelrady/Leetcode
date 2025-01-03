class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            prefix.append(prefix[i-1] + nums[i])

        cnt = 0 

        for i in range(n-1):
            if prefix[i] >= prefix[n-1] - prefix[i]:
                cnt += 1

        return cnt       
       