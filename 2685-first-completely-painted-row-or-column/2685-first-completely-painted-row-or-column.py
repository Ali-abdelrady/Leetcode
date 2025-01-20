class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS,COLS  = len(mat) , len(mat[0])
        painted_rows = [0]*ROWS
        painted_cols = [0]*COLS
        mp = {}
        for i in range(ROWS):
            for j in range(COLS):
                mp[mat[i][j]] = (i,j)

        for i in range(len(arr)) :
            r,c = mp[arr[i]]
            painted_cols[c] += 1
            painted_rows[r] += 1
            if painted_cols[c] == ROWS or painted_rows[r] == COLS :
                return i   