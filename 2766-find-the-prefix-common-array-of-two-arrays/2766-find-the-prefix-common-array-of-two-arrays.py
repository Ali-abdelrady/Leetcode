class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0]*n
        freq = {}

        for i in range(n):
            res[i] = res[i-1] if i > 0 else 0
            if A[i] in freq:
                res[i] += 1
            else:
                freq[A[i]] = 1
            if B[i] in freq:
                res[i] += 1
            else:
                freq[B[i]] = 1

        return res 