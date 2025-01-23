class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid) , len(grid[0])
        rowServers = [0]*ROWS
        colServers = [0]*COLS
        q = deque([])
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    q.append((i,j))
                    rowServers[i] += 1 
                    colServers[j] += 1

        while q :
            r,c = q.popleft()
            if rowServers[r] > 1 or colServers[c] > 1:
                res += 1

        return res
