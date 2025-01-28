class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])

        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]]

        q = deque([])
        visited = set()
        res = 0
        def bfs(pair):
            nonlocal res
            sum = 0
            visited.add(pair)
            q.append(pair)
            while q:
                r , c = q.popleft()
                sum += grid[r][c]
                for d in directions:
                    nr , nc = r + d[0] , c + d[1]
                    if( nr == ROWS or nc == COLS or
                        nr < 0 or nc < 0
                        or grid[nr][nc] == 0 or (nr,nc) in visited):
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))
            res = max(res,sum)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] and (i,j) not in visited:
                    bfs((i,j))

        return res        