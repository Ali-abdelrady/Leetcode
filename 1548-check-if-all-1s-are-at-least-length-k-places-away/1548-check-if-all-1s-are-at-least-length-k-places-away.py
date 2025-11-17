class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastOneIdx = -1
        for i in range(len(nums)):
            if nums[i]:
                if lastOneIdx != -1 and i - lastOneIdx - 1 < k:
                    return False
                lastOneIdx = i
        return True        