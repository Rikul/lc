import numpy as np
from collections import Counter
import time

class Solution:


    ## Not working
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m = len(isWater)
        n = len(isWater[0])
        land = []
        water = []

        print(time.time())

        for i in range(m):
            for j in range(n):
                isWater[i][j] = 0 if isWater[i][j] == 1 else 1
                if isWater[i][j] == 0:
                    water.append((i,j))

        print(time.time())
        for i,j in water:
                neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                if isWater[i][j] == 0:
                    has_land = False    
                    for x,y in neighbors:
                        if 0 <= x < m and 0 <= y < n:
                            if isWater[x][y] == 1:
                                has_land = True
                                land.append((x,y))
        
        print(time.time())         
        print(water,land)
    
        
        for br,bc in land | water:
            q = [(br,bc)]
            visited = set([(br,bc)])        
            map_changed = False
            print(time.time())

            while q:
                r,c = q.pop(0)
                heights = []
                neighbors = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

                for i,j in neighbors:
                    if 0 <= i < m and 0 <= j < n:
                        heights.append(isWater[i][j])
                        if (i,j) not in visited:
                            q.append((i,j))
                            visited.add((i,j))
                
                min_height = min(heights)
                if heights and isWater[r][c] != 0:
                    if isWater[r][c] != min_height+1:
                        isWater[r][c] = min_height + 1
                        map_changed = True
        
            if not map_changed: 
                break
                


        return isWater