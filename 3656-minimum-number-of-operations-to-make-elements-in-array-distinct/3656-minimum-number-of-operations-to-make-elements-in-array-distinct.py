class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums) 
        i = n - 1
        seen = {}
        while i >= 0 and nums[i] not in seen:
            seen[nums[i]] = True
            i -= 1

        operations = i // 3 + 1

        return operations   