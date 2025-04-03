class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0]*n
        suffix_max = [0]*n

        i = 0
        j = n - 1
        for k in range(n):
            if k == 0 :
                prefix_max[i] = nums[i]
                suffix_max[j] = nums[j]
            else:
                prefix_max[i] = max(prefix_max[i-1] , nums[i] )
                suffix_max[j] = max(suffix_max[j+1] , nums[j] )
            i += 1
            j -= 1

        res = 0
        for j in range(1,n-1):
            res = max(res , (prefix_max[j-1] - nums[j]) * suffix_max[j+1])


        return  res        