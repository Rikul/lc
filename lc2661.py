class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        nrows = len(mat)
        ncols = len(mat[0])    
        rows_painted = [0] * nrows
        columns_painted = [0] * ncols
        all_nums = [0] * (nrows * ncols + 1)

        for i in range(nrows):
            for j in range(ncols):
                all_nums[mat[i][j]] = (i,j)
        
        for i,n in enumerate(arr):
            r,c = all_nums[n]
            rows_painted[r] += 1
            columns_painted[c] += 1
            
            if rows_painted[r] >= ncols:
                return i

            if columns_painted[c] >= nrows:
                return i

        return 0