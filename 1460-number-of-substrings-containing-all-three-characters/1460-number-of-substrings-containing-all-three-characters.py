class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l , r = 0 , 0
        n = len(s)
        mp = defaultdict(int)
        res = 0 
        while l < n and r < n:
            # Check if it's valid
            mp[s[r]] += 1
            while mp['a'] > 0 and mp['b'] > 0 and mp['c'] > 0:
                res += n - r
                mp[s[l]] -= 1
                l += 1
            
            # The Window is invalid
            r += 1

        return res        