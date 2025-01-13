class Solution:
    def minimumLength(self, s: str) -> int:
        res = len(s)
        mp = {}
        for ch in s :
            if not ch in mp:
                mp[ch] = 1
            else:
                if mp[ch] < 2:
                    mp[ch] += 1
                else:
                    mp[ch] -= 1
                    res -= 2

        return res       