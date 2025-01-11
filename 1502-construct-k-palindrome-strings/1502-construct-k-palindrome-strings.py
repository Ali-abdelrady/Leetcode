class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k :
            return False
        mp = Counter(s)
        odd_cnt = 0
        for key,value in mp.items():
            if value % 2 != 0:
                odd_cnt += 1
            if odd_cnt > k :
                return False
    
        return True