class Solution:
    def countOdds(self, low: int, high: int) -> int:
        numCnt = high - low + 1
        if numCnt % 2 == 0:
            return numCnt // 2
        
        div = numCnt // 2
        return div if low % 2 == 0 else div + 1