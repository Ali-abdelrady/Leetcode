class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0]) ** 2
        total_sum =int(n * (n+1) / 2)
        mp = defaultdict(int)
        a , b = 0 , 0 
        sum = 0
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                if grid[i][j] in mp:
                    a = grid[i][j]
                else:
                    mp[grid[i][j]] += 1
                    sum += grid[i][j]

        b = total_sum - sum
        return [a,b]        