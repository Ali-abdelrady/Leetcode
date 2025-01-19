class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        ]
        q = deque([])
        max_area = 0
        visited = set()
        ROWS,COLS = len(grid) , len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    area = 0
                    while q:
                        r , c = q.popleft()
                        area += 1
                        
                        for dr,dc in directions:
                            nr,nc = r + dr , c + dc
                            if (
                                0 <= nr < ROWS
                                and  0 <= nc < COLS 
                                and grid[nr][nc] == 1
                                and (nr,nc) not in visited
                            ):
                                q.append((nr,nc))
                                visited.add((nr,nc))
                                
                    max_area = max(max_area , area)

        return max_area