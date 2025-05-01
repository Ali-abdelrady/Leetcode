class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(Counter(nums)) 
        l = 0
        n = len(nums)
        mp = defaultdict(int)
        res = 0 
        for r in range(n):
            mp[nums[r]] += 1
            while len(mp) == k :
                res += n - r
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    del mp[nums[l]]
                l += 1

        return  res        