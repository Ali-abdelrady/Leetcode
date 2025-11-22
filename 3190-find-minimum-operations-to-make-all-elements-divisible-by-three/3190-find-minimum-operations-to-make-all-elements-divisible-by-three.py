class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        op = 0
        for num in nums:
            if num % 3 != 0:
                op += 1
        return op 
        