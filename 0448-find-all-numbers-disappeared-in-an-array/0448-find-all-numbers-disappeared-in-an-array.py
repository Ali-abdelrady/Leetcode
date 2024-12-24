class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mp = {}

        for num in nums :
            if num not in mp :
                mp[num] = True

        res = []
        cnt = 1
        while cnt <= len(nums):
            if cnt not in mp :
                res.append(cnt)    
            cnt += 1

        print(res)
        return res

          