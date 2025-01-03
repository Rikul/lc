class Solution:
    
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m : int = len(grid)      # Number of rows
        n : int = len(grid[0])   # Number of cols
        end  = (m-1,n-1)
        q : list[tuple(int,int,int)] = [(0,0,health - grid[0][0])]
        visited = [(0,0)]
        
        while len(q):
            (r,c,current_health) = q.pop(0)
            print("queue ",r,c, current_health)

            if current_health - grid[r][c] <= 0:
                continue
                
            if (r,c) == end:
                return True
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                safeCells = []
                allCells = []
               
                if (0 <= nr < m) and (0 <= nc < n) and (nr,nc) not in visited:
                    if grid[nr][nc] == 0:
                        safeCells.append((nr,nc, current_health-grid[r][c]))
                    else:
                        allCells.append((nr,nc, current_health-grid[r][c]))

                    if len(safeCells) > 0:
                        q = safeCells + q
                        for r,c,h in safeCells:
                            visited += [(r,c)]
                    if len(allCells) > 0:
                        q.extend(allCells)
                        for r,c,h in allCells:
                            visited += [(r,c)]
                    
        return False
    