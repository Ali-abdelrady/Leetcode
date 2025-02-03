class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = False
        for i in range(len(nums)):
            next = 0 if i == len(nums)-1 else i+1
            if nums[i] > nums[next]:
                if flag:
                    return False
                else:
                    flag = True

        return True        