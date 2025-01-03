class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        xo = ['A','B']
        pending = len(moves) < 9
        
        for i,m in enumerate(moves):
            grid[m[0]][m[1]] = xo[i % 2]
        
        for x in range(3):
            row = "".join(grid[x])
            col = grid[0][x] + grid[1][x] + grid[2][x]
            
            if row == "AAA" or row == "BBB":
                return row[0]
            
            if col == "AAA" or col == "BBB":
                return col[0]
            
        d = grid[0][0] + grid[1][1] + grid[2][2]
        if  d == "AAA" or d == "BBB":
            return d[0]
        
        d = grid[0][2] + grid[1][1] + grid[2][0]
        if  d == "AAA" or d == "BBB":
            return d[0]
        
        
        return "Draw" if pending == False else "Pending"