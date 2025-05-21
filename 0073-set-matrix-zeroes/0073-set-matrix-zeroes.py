class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M , N = len(matrix) , len(matrix[0])
        zeroRows = set()
        zeroCols = set()

        for row in range(M):
            for col in range(N):
                if matrix[row][col] == 0:
                    zeroRows.add(row)
                    zeroCols.add(col)


        for row in zeroRows:
            for col in range(N) :
                matrix[row][col] = 0 

        for col in zeroCols:
            for row in range(M):
                matrix[row][col] = 0 

        return matrix      
        