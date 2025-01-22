class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]
        INT_MAX = sys.maxsize
        ROWS,COLS = len(isWater) , len(isWater[0])
        heights = [[INT_MAX for _ in range(COLS)]for _ in range(ROWS)]
        q = deque([])
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j] == 1 :
                    q.append((i,j))

        while q:
            r,c = q.popleft()

            min_num = INT_MAX
            for d in directions:
                nr,nc = d[0] + r , d[1] + c
                if (
                    nr < 0 or nc < 0
                    or nr == ROWS or nc == COLS
                ):
                    continue
                min_num = min(min_num,heights[nr][nc])
                
                if (nr,nc) not in visited:
                    q.append((nr,nc))
                    visited.add((nr,nc))

            heights[r][c] = min_num + 1 if isWater[r][c] == 0 else 0

        return heights        