class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        white_prefix = [0]*(n+1)

        for i , ch in enumerate(blocks):
            if ch == 'W':
                white_prefix[i+1] = white_prefix[i] + 1
            else:
                white_prefix[i+1] = white_prefix[i]

        i , j = 0 , k
        res = sys.maxsize
        while j <= n :
            if res == 0 :
                return 0
            op = white_prefix[j] - white_prefix[i]
            res = min(op , res)
            i += 1
            j += 1

        return res        