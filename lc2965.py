from collections import Counter
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        ct = Counter()
        ct.update([grid[i][j] for i in range(n) for j in range(n)])
        res = [-1,-1]

        for y in [x for x in range(1,n**2 + 1)]:

            if ct[y] != 1:

                if ct[y] > 1:
                    res[0] = y
                elif ct[y] == 0:
                    res[1] = y

                
                if res[0] != -1 and res[1] != -1:
                    return res

        return res