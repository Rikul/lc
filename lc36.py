from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def valid9(grp : List[str]):
            return sorted(set(grp)) == sorted(grp)
        
        for r in range(0,9):
            if not valid9([c for c in board[r] if c != '.']): return False
            column = [board[c][r] for c in range(0,9) if board[c][r] != '.']
            if not valid9(column): return False
            
        for r in (0,3,6):
            for c in (0,3,6):
                cell9 = [board[r+i][c+j] for i in (0,1,2) for j in (0,1,2) if board[r+i][c+j] != '.']
                if not valid9(cell9): return False
                
        return True