class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i = 0
        j = i+1
        maxInc , maxDec = 1 , 1
        sumInc , sumDec = 1 , 1 

        while i < len(nums) - 1:
            print(sumInc,sumDec)
            # Check if its incraesing
            if nums[i] < nums[i+1]:
                sumDec = 1
                sumInc += 1
                maxInc = max(maxInc,sumInc)
            elif nums[i] > nums[i+1]:
                sumInc = 1
                sumDec += 1
                maxDec = max(maxDec,sumDec)
            else:
                sumInc = 1
                sumDec = 1
            i += 1
        print(maxDec,maxInc)
        return max(maxDec,maxInc)