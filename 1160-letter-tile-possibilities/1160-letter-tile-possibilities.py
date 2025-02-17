class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        mp = Counter(tiles)

        def backtrack():
            res = 0
            
            for ch in mp.keys():
                if mp[ch] > 0:
                    mp[ch] -= 1 
                    res += 1 + backtrack()
                    mp[ch] += 1
            return res 
        return backtrack()        