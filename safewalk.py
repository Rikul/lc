import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = None,None

def visualize(grid, current, visited):
    global fig, ax

    if fig is None:
        fig, ax = plt.subplots()
    
    ax.clear()
    
    white_grid = np.ones_like(grid, dtype=int)
    ax.imshow(white_grid, cmap='Greys', interpolation='none')
    
    # Change the color of visited cells to green
    for (r, c) in visited:
        ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, fill=True, color='green'))
    
    # Mark the current cell with 'O' in blue
    ax.text(current[1], current[0], 'O', ha='center', va='center', color='blue')
    
    # Remove x and y labels
    ax.set_xticks(np.arange(-.5, len(grid), 1))
    ax.set_yticks(np.arange(-.5, len(grid), 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    # Add grid lines
    ax.grid(color='black', linestyle='-', linewidth=1)
    
    plt.pause(1)


class Solution:
    
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m : int = len(grid)      # Number of rows
        n : int = len(grid[0])   # Number of cols
        end  = (m-1,n-1)
        q : list[tuple(int,int,int)] = [(0,0,health)]
        visited = {(0,0)}
        
        print(end)
        while len(q):
            (r,c,current_health) = q.pop(0)
            
            print(r,c,current_health)
            #if current_health - grid[r][c] <= 0:
            #    continue

            if (r,c) == end and current_health >= 1:
                return True
                    
            
            safeCells = []
            allCells = []
                
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 

                visualize(grid, (r, c), visited)
                
                if (0 <= nr < m) and (0 <= nc < n) and (nr,nc) not in visited:
                    
                    if (nr,nc) == end:
                        if current_health - grid[nr][nc] >= 1:
                            return True 

                    q.append((nr,nc,current_health - grid[nr][nc]))
                    visited.add((nr,nc))

                """

                    if (0 <= nr < m) and (0 <= nc < n) and (nr,nc) not in visited:
                        if grid[nr][nc] == 0:
                            safeCells.append((nr,nc, current_health-grid[r][c]))
                        else:
                            allCells.append((nr,nc, current_health-grid[r][c]))

                    if len(safeCells) > 0:
                        q = safeCells + q
                        for r,c,h in safeCells:
                            visited.add((r,c))

                    if len(allCells) > 0:
                        q.extend(allCells)
                        for r,c,h in allCells:
                            visited.add((r,c))
        
                    """

        return False


def main():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    health = 25
    solution = Solution()
    result = solution.findSafeWalk(grid, health)
    print("Path found:", result)
    plt.show()

if __name__ == "__main__":
    main()
    