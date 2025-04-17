class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_mp = defaultdict(list)
        res = 0 
        for i in range(len(nums)):
            for j in index_mp[nums[i]]:
                if i * j % k == 0:
                    res += 1
            index_mp[nums[i]].append(i)
        return res    