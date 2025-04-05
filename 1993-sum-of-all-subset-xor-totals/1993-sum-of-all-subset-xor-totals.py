class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,sum):
            #base case
            if i == len(nums):
                return sum
            
            include =  dfs(i+1,nums[i] ^ sum)
            exclude = dfs(i+1,sum)

            return  include + exclude
        return dfs(0,0)