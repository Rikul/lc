import tkinter as tk
import time
import heapq

class Solution:
        
    def __init__(self):
        self.visited = []

    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m : int = len(grid)      # Number of rows
        n : int = len(grid[0])   # Number of cols
        end : (int,int) = (m-1,n-1)
        q : list[(int,int,int)] = []
        visited = set((0,0))
        
        heapq.heappush(q, (grid[0][0],0,0))
        
        while q:
            cost,r,c = heapq.heappop(q)
           
            if health - cost <= 0:
                continue
            
            self.update_grid(r, c)

            if (r,c) == end:
                return True
            
            for (_r,_c) in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (0 <= _r < m) and (0 <= _c < n) and (_r,_c) not in visited:
                    heapq.heappush(q,(cost + grid[_r][_c], _r, _c))
                    visited.add((_r, _c))
               
        return False
    
        
    def create_grid(self, rows, cols):
        self.root = tk.Tk()
        self.root.title("Safe Walk Visualization")
        self.root.geometry("500x500")  # Set window size to 500x500

        self.frames = [[tk.Frame(self.root, width=(500-cols*2)//cols, height=(500-rows*2)//rows, bg='white', relief='solid', borderwidth=1) for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                self.frames[r][c].grid(row=r, column=c, padx=1, pady=1)

        self.root.update()

    def update_grid(self, r, c):
     
        self.frames[r][c].config(bg='lightblue')
        self.root.update()


def main():


    grid = [[0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1],[0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1],[1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,1,0],[0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0],[1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1],[1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,1,1,0,1],[1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,1,1],[0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1],[0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,0],[0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0],[1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1],[0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1],[1,1,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,0],[0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,1],[1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0]]
    health = 50

    solution = Solution()
    solution.create_grid(len(grid), len(grid[0]))
    if solution.findSafeWalk(grid, health):
        print("Path found")

    solution.root.mainloop()

if __name__ == "__main__":
    main()