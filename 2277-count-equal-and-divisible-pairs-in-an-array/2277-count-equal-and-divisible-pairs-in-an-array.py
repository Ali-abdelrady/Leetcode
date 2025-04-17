class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        mp = {}
        res = 0 
        for index,num in enumerate(nums):
            if num in mp:
                arr = mp[num]
                for i in arr:
                    if i * index % k == 0:
                        res += 1
                mp[num].append(index)
            else:
                mp[num]= [index]

        return res    