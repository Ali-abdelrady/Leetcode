class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for num in nums : 
            if num in mp :
                mp[num] += 1
            else:
                mp[num] = 1
        
        res = 0
        max_value = 0
        for (key , value) in mp.items():
            if value > max_value:
                res = key
                max_value = value
        return res 