class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mp = {}
        res = 0
        for domino in dominoes:
            a , b = sorted(domino)
            if (a,b) in mp:
                res += mp[(a,b)]
                mp[(a,b)] += 1
            else:
                mp[(a,b)] = 1
        return res      