class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def binary_search(target):
            i,j = 0,len(nums)-1
            while i <= j :
                mid = int(i + (j - i) / 2)
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            return  False

        nums.sort()
        cnt = 1 
        res = []
        while cnt <= len(nums):
            if not binary_search(cnt):
                res.append(cnt)
            cnt += 1

        return res

          